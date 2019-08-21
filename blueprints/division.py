from flask_restplus import Namespace, Resource
division_namespace = Namespace('division', description='Division Operation')

# Division --------------------------------------------------------------------+
division_parser = division_namespace.parser()
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

    @division_namespace.doc(parser=division_parser)
    def post(self):
        div_args = division_parser.parse_args()
        division_name = div_args['divname']
        Divisions.append(division_name)
        return {'msg':'new division is created','division': division_name}
