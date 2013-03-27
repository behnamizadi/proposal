# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    page=1
    if request.vars['page']:
        page=max(page,int(request.vars['page']))
    items=10
    limit=((page-1)*items,((page)*items)+1)
    proposals = db(db.proposal).select(limitby=limit)
    pr=[]
    for p in proposals:
        l=len(db(db.like.proposal==int(p.id)).select())
        pr.append([p.id,p.title,p.created_by,l])

    return dict(pr=pr,page=page,items_per_page=items)

@auth.requires_login()
def create():
   form=SQLFORM(db.proposal).process(next=URL('index'))
   return dict(form=form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)

def addlike():
    """
    add a plus like to a proposal
    """
    l=0
    userid=auth.user_id
    ids=request.vars['proposal']
    l=db((db.like.proposal==ids)&(db.like.author==userid)).count()
    if l>0:
        return '%s can not add another like. current=%s' %(ids,l)
    else:
        db.like.insert(like=1,author=userid,proposal=ids)
        return 'added %s'% ids


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
