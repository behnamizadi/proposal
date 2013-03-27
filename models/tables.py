#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('proposal',
    Field('title'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')

db.proposal.title.requires = IS_NOT_IN_DB(db, 'proposal.title')
db.proposal.body.requires = IS_NOT_EMPTY()
db.proposal.created_by.readable = db.proposal.created_by.writable = False
db.proposal.created_on.readable = db.proposal.created_on.writable = False

#########################################################################

db.define_table('lyke',
    Field('author','reference auth_user'),
    Field('lyke','integer'),
    Field('proposal','reference proposal'))
