from schema import LearnerSchema

json_data = """
[
    {
		"uid": 1,
		"name": "Alex",
		"final_test": "True"
	},
	{
		"uid": 2,
		"name": "Ivan",
		"final_test": "True"
	},
	{
		"uid": 4,
		"name": "Tom",
		"final_test": "False"
	}
]
"""

# json_data = """
# {
#     "uid": 4,
#     "name": "Tom",
#     "final_test": "False"
# }
# """

try:
    schema = LearnerSchema()
    result = schema.loads(json_data)
except:
    schema = LearnerSchema(many=True)
    result = schema.loads(json_data)

print(result, type(json_data))
