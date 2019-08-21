from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Member API',
    description='A simple Member API',
)

member_namespace = api.namespace('member', description='Member Operation')
division_namespace = api.namespace('division', description='Division Operation')


# Member ----------------------------------------------------------------------+
member_parser = api.parser()
Members = {
    'member1': {'name': 'William', 'callsign': 'Eagle'},
    'member2': {'name': 'Natsuko', 'callsign': 'Dragon'},
    'member3': {'name': 'Seth', 'callsign': 'Wolf'},
}
def abort_if_member_not_exist(member_id):
    if member_id not in Members:
        member_namespace.abort(404, "Member {} doesn't exist".format(member_id))

member_parser.add_argument('member_name', type=str, required=True, help="The name of the member", location="form")
member_parser.add_argument('member_callsign', type=str, required=True, help="The Callsign of the member", location="form")

@member_namespace.route('/<string:member_id>')
class Member_manage(Resource):
    @member_namespace.doc(description="member_id yang tersedia <b>{}</b>".format(','.join(Members.keys())))
    def get(self, member_id):
        ''' Melihat detail member '''
        abort_if_member_not_exist(member_id)
        return Members[member_id]

    @member_namespace.doc(parser=member_parser)
    def put(self, member_id):
        ''' Merubah info member '''
        abort_if_member_not_exist(member_id)
        member_args = member_parser.parse_args()
        memberinfo = {'name': member_args['member_name'], 'callsign': member_args['member_callsign']}
        Members[member_id] = memberinfo
        return memberinfo

    def delete(self, member_id):
        ''' menghapus member '''
        abort_if_member_not_exist(member_id)
        member_name = Members[member_id]['name']
        del Members[member_id]
        return {'msg':'{} Membership has been revoked'.format(member_name)}

@member_namespace.route('/')
class Member_creation(Resource):
    def get(self):
        ''' Melihat Data semua Member '''
        return {'data':Members}

    @api.doc(parser=member_parser)
    def post(self):
        ''' Membuat Member baru '''
        member_args = member_parser.parse_args()
        memberinfo = {'name': member_args['member_name'], 'callsign': member_args['member_callsign']}
        member_id = "member{}".format( len(Members.items()) + 1 )
        Members[member_id] = memberinfo
        return {'msg':memberinfo}

# Division --------------------------------------------------------------------+
division_parser = api.parser()
Divisions = [
    'Research & Developent',
    'Medical Unit',
    'Technical Unit',
    'Experimental Warfare',
    'Electronical Warfare',
    'Valkyrie',
    'Night Witch',
    'Rabbit',
    'Ghosts'
]
@division_namespace.route('/')
class Division_manage(Resource):
    division_parser.add_argument('divname', type=str, required=True, help="Name of the Division")

    def get(self):
        return {'data': Divisions}

    @api.doc(parser=division_parser)
    def post(self):
        div_args = division_parser.parse_args()
        division_name = div_args['divname']
        Divisions.append(division_name)
        return {'msg':'new division is created','division': division_name}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)