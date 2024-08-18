from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.chat_service import ChatService

authorizations = {
    "jsonWebToken" : {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

api = Namespace('chat', description='Chat operations', authorizations=authorizations)

message_model = api.model('Message', {
    'message': fields.String(required=True, description='Chat message')
})

chat_message_model = api.model('ChatMessage', {
    'message_id': fields.Integer,
    'message_text': fields.String,
    'sender': fields.String,
    'timestamp': fields.DateTime
})

conversation_model = api.model('Conversation', {
    'conversation_id': fields.Integer,
    'title': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
})

conversation_detail_model = api.inherit('ConversationDetail', conversation_model, {
    'messages': fields.List(fields.Nested(chat_message_model))
})

new_chat_response_model = api.model('NewChatResponse', {
    'conversation': fields.Nested(conversation_model),
    'user_message': fields.Nested(chat_message_model),
    'ai_message': fields.Nested(chat_message_model)
})

continue_chat_response_model = api.model('ContinueChatResponse', {
    'user_message': fields.Nested(chat_message_model),
    'ai_message': fields.Nested(chat_message_model)
})

@api.route('/conversations')
class ConversationList(Resource):
    @api.marshal_list_with(conversation_model)
    @api.doc(security="jsonWebToken")
    @jwt_required()
    def get(self):
        """Get all conversations for the current user"""
        student_id = get_jwt_identity()
        conversations = ChatService.get_student_conversations(student_id)
        return conversations, 200

@api.route('/conversations/<int:conversation_id>')
class Conversation(Resource):
    method_decorators = [jwt_required()]

    @api.marshal_with(conversation_detail_model)
    @api.doc(security="jsonWebToken")
    def get(self, conversation_id):
        """Get a specific conversation with all its messages"""
        student_id = get_jwt_identity()
        conversation = ChatService.get_conversation(conversation_id, student_id)
        if not conversation:
            api.abort(404, "Conversation not found")
        if conversation.student_id != student_id:
            api.abort(403, "Unauthorized to access this conversation")
        return conversation, 200
    
    @api.doc(security="jsonWebToken")
    def delete(self, conversation_id):
        """Delete a specific conversation"""
        student_id = get_jwt_identity()
        conversation = ChatService.get_conversation(conversation_id, student_id)
        if not conversation:
            api.abort(404, "Conversation not found")
        if conversation.student_id != student_id:
            api.abort(403, "Unauthorized to delete this conversation")
        ChatService.delete_conversation(conversation_id, student_id)
        return {"message" : "Conversation deleted successfully"}, 200


@api.route('/start')
class StartNewChat(Resource):
    @api.expect(message_model)
    @api.marshal_with(new_chat_response_model)
    @api.doc(security="jsonWebToken")
    @jwt_required()
    def post(self):
        """Start a new conversation"""
        student_id = get_jwt_identity()
        message = api.payload['message']

        try:
            conversation, user_message, ai_message = ChatService.start_new_conversation(student_id, message)
            return {
                'conversation': conversation,
                'user_message': user_message,
                'ai_message': ai_message
            }, 201
        except ValueError as e:
            api.abort(400, str(e))

@api.route('/continue/<int:conversation_id>')
class ContinueChat(Resource):
    @api.expect(message_model)
    @api.marshal_with(continue_chat_response_model)
    @api.doc(security="jsonWebToken")
    @jwt_required()
    def post(self, conversation_id):
        """Continue an existing conversation"""
        student_id = get_jwt_identity()
        message = api.payload['message']

        conversation = ChatService.get_conversation(conversation_id, student_id)
        if not conversation:
            api.abort(404, "Conversation not found")
        if conversation.student_id != student_id:
            api.abort(403, "Unauthorized to access this conversation")

        try:
            user_message, ai_message = ChatService.continue_conversation(student_id, conversation_id, message)
            return {
                'user_message': user_message,
                'ai_message': ai_message
            }, 200
        except ValueError as e:
            api.abort(400, str(e))
