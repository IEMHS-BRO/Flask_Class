from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from app import db
from app.models.product import Product
from app.models.user import User
from app.utils.image_utils import save_image, delete_image

bp = Blueprint('product', __name__, url_prefix='/products')


'''
제품 목록 획득
'''
@bp.route('/', methods=['GET'])
@jwt_required()
def get_products():
    if 'authenticated' in request.args and request.args['authenticated'].lower() == 'true':
        user_id = get_jwt_identity()
        products = Product.query.filter_by(user_id=user_id).all()
    else:
        products = Product.query.all()
    
    return jsonify(products=[product.serialize() for product in products]), 200


'''
제품 등록
'''
@bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    json_data = request.form.get('json_data')
    data = json.loads(json_data)
    image_url = save_image(request.files['image'])
    new_product = Product(
        image_url=image_url,
        title=data['title'],
        price=data['price'],
        description=data['description'],
        user_id=get_jwt_identity()
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify(new_product.serialize()), 201


'''
제품 정보 획득
'''
@bp.route('/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product_info(product_id):
    product = Product.query.get(product_id)
    return jsonify(product.serialize()), 200


'''
제품 정보 수정
'''
@bp.route('/<int:product_id>', methods=['POST'])
@jwt_required()
def update_product_info(product_id):
    print(request.files)
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'msg': 'Product not found'}), 404
    if product.user_id != get_jwt_identity():
        return jsonify({'msg': 'Not authorized to update this product'}), 403

    json_data = request.form.get('json_data')
    data = json.loads(json_data)

    if product.image_url:
        delete_image(product.image_url)
    updated_image_url = save_image(request.files['image'])
    product.image_url = updated_image_url
    
    product.title = data['title']
    product.price = data['price']
    product.description = data['description']
    db.session.commit()

    return jsonify(product.serialize()), 200


'''
제품 삭제
'''
@bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'msg': 'Product not found'}), 404
    if product.user_id != get_jwt_identity():
        return jsonify({'msg': 'Not authorized to delete this product'}), 403

    # 이미지 삭제
    if product.image_url:
        delete_image(product.image_url)

    db.session.delete(product)
    db.session.commit()

    return jsonify({'msg': 'Product deleted successfully'}), 200