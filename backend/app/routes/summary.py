from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from app.services.summary_service import SummaryService

authorizations = {
    "jsonWebToken" : {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

api = Namespace('summary', description='AI Lecture Summaries', authorizations=authorizations)

summary_model = api.model('Summary', {
    'summary': fields.String(required=True, description='Lecture summary')
})

@api.route('/<int:content_id>')
class Summary(Resource):
    @api.doc(security="jsonWebToken")
    @jwt_required()
    @api.marshal_with(summary_model)
    def get(self, content_id):
        """Get a summary for a lecture using its content_id"""
        summary = SummaryService.generate_summary(content_id)
        if not summary:
            api.abort(404, "Lecture transcript unavailable, summary generation failed")
        return summary, 200