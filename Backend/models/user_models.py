from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(
        db.Enum("user", "admin", name="user_roles"),
        default="user"
    )

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # Relationships
    prompts = db.relationship(
        "Prompt",
        backref="user",
        cascade="all, delete-orphan"
    )

    logs = db.relationship(
        "ActivityLog",
        backref="user",
        passive_deletes=True
    )

    def __repr__(self):
        return f"<User {self.username}>"
    

class Prompt(db.Model):
    __tablename__ = "prompts"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    chat_id = db.Column(db.String(50), index=True)  # index added

    prompt_text = db.Column(db.Text, nullable=False)

    prompt_type = db.Column(
        db.Enum("search", "summary", "quiz", "mcqs", "flashcards", "explain", name="prompt_types"),
        default="search"
    )

    status = db.Column(
        db.Enum("pending", "processing", "completed", "failed", name="prompt_status"),
        default="pending"
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    response = db.relationship(
        "Response",
        backref="prompt",
        uselist=False,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Prompt {self.id}>"
    
    
class Response(db.Model):
    __tablename__ = "responses"  # FIXED

    id = db.Column(db.Integer, primary_key=True)

    prompt_id = db.Column(
        db.Integer,
        db.ForeignKey("prompts.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    result_text = db.Column(db.Text, nullable=False)
    confidence_score = db.Column(db.Float)

    processing_time_ms = db.Column(db.Integer)
    model_used = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Response prompt_id={self.prompt_id}>"


class PromptHistory(db.Model):
    __tablename__ = "prompt_history"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    prompt_id = db.Column(
        db.Integer,
        db.ForeignKey("prompts.id", ondelete="CASCADE"),
        nullable=False
    )

    viewed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PromptHistory user={self.user_id} prompt={self.prompt_id}>"


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="SET NULL")
    )

    action = db.Column(db.String(100))
    description = db.Column(db.Text)

    ip_address = db.Column(db.String(45))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ActivityLog {self.action}>"


class ApiToken(db.Model):
    __tablename__ = "api_tokens"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    token_hash = db.Column(db.String(255), nullable=False)
    expires_at = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ApiToken user_id={self.user_id}>"
       
    
class UserPreferences(db.Model):
    __tablename__ = "user_preferences"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    learning_style = db.Column(db.String(20), default="text")
    difficulty_level = db.Column(db.String(20), default="medium")
    daily_goal_minutes = db.Column(db.Integer, default=30)
    preferred_task = db.Column(db.String(20), default="summary")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship("User", backref="preferences", uselist=False)
