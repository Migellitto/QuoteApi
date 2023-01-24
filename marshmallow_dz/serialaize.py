from learner import Learner
from schema import LearnerSchema


learners = [
    Learner(1, "Alex", True),
    Learner(1, "Xela", True),
    Learner(1, "Xlea", False)
]

# learners = Learner(1, "Xlea", False)

try:
    learner_schema = LearnerSchema(many=True)
    result = learner_schema.dump(learners)
except:
    learner_schema = LearnerSchema()
    result = learner_schema.dump(learners)

print(result, type(result))
