from flask import jsonify, request

from ..user import user


# TODO define users model
users = [
    {
        'name': 'Corentin',
        'accounts': []
    },
    {
        'name': 'Austin',
        'accounts': []
    }
]


def model_user_verify(input):
    if 'name' not in input:
        raise Exception('Name is mandatory')


@user.route('/', methods=['GET'])
def get_root():
    return jsonify({'users': users})


@user.route('/', methods=['POST'])
def post_root():
    model_user_verify(request.json)
    users.append(request.json)
    return 200


@user.route('/<userid>', methods=['PUT'])
def put_user(userid):
    new_user = request.json
    model_user_verify(new_user)
    users[userid] = new_user
    return 200


@user.route('/<userid>', methods=['GET'])
def get_user(userid):
    return jsonify(users[userid])


@user.route('/<userid>', methods=['DELETE'])
def delete_user(userid):
    del users[userid]
    return 200