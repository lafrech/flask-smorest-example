"""Teams resources"""

from flask.views import MethodView

from team_manager.extensions.api import Blueprint, SQLCursorPage
from team_manager.extensions.database import db
from team_manager.models import Team, Member

from .schemas import TeamSchema, TeamQueryArgsSchema


blp = Blueprint(
    'Teams',
    __name__,
    url_prefix='/teams',
    description="Operations on teams"
)


@blp.route('/')
class Teams(MethodView):

    @blp.etag
    @blp.arguments(TeamQueryArgsSchema, location='query')
    @blp.response(200, TeamSchema(many=True))
    @blp.paginate(SQLCursorPage)
    def get(self, args):
        """List teams"""
        member_id = args.pop('member_id', None)
        ret = Team.query.filter_by(**args)
        if member_id is not None:
            ret = ret.join(Team.members).filter(Member.id == member_id)
        return ret

    @blp.etag
    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, new_item):
        """Add a new team"""
        item = Team(**new_item)
        db.session.add(item)
        db.session.commit()
        return item


@blp.route('/<uuid:item_id>')
class TeamsById(MethodView):

    @blp.etag
    @blp.response(200, TeamSchema)
    def get(self, item_id):
        """Get team by ID"""
        return Team.query.get_or_404(item_id)

    @blp.etag
    @blp.arguments(TeamSchema)
    @blp.response(200, TeamSchema)
    def put(self, new_item, item_id):
        """Update an existing team"""
        item = Team.query.get_or_404(item_id)
        blp.check_etag(item, TeamSchema)
        TeamSchema().update(item, new_item)
        db.session.add(item)
        db.session.commit()
        return item

    @blp.etag
    @blp.response(204)
    def delete(self, item_id):
        """Delete a team"""
        item = Team.query.get_or_404(item_id)
        blp.check_etag(item, TeamSchema)
        db.session.delete(item)
        db.session.commit()
