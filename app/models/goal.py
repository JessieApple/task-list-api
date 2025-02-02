from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal", lazy=True)
    
    def to_dict(self):
        tasks = [task.to_dict() for task in self.tasks]
        goal_as_dict = {}
        goal_as_dict['id'] = self.goal_id
        goal_as_dict['title'] = self.title
        goal_as_dict["tasks"] = tasks 
        
        return goal_as_dict
