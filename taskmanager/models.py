from taskmanager import db


class Category(db.model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        # self representation or description of itself
        return self.category.name


class Task(db.model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(25), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable = False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), ondelete="CASCADE", nullable=False)

    def __repr__(self):
        # self representation or description of itself
        return f"#{self.id} - Task: {self.task_name} urgent: {self.is_urgent}"
