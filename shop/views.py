import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required 
from .models import ItemImage,seller_product,cartItems
from account.models import Seller
from django.http import JsonResponse,HttpResponse
from django.utils import timezone

# Create your views here.zz
# @login_required
def handle_basic_request(request):
  # print('handle basic start')
  user = {}
  # print("it is request handeler")
  try:
    user = {
      'user_name' : f'{request.user.first_name} {request.user.last_name}',
      'user_email' : request.user.email,
      'user_type' : request.user.role,
    }
    # print(f'user retrived data :- {user} ')
    # print("it is end of handeler ")
    # print('handle basic end')

  except:
    print("unauthorize persion try to acces ")
  return user

@csrf_exempt
def json_data_for_homepage_products(request):
  # print('json of home fun start')
  product_data = []
  product_details = seller_product.objects.order_by('?')[:6]

  for product in product_details:
    try:
      img = ItemImage.objects.filter(related_product = product)[0].image.url
      # print(f'first image url is -- {img}')
      # print(f'the title of the product - {product.item_name}')
    except:
      img = ""
    product_data.append({"titel":product.item_name,'id':product.product_id,'price':product.price ,'image':img })
  # print(product_data)
    # print('handle basic fun end')
  return product_data

def home(request):
  return render(request,'most_use_pages/home.html',{'user_data':handle_basic_request(request),'product_items':json_data_for_homepage_products(request)})


@login_required
def item_review(request):
  # Dinamic 
  ...


@csrf_exempt
@login_required
def upload_item(request):
  print("now in upload item page .........")
  print(f'Request type : {request.method}')
  try:
    if request.method == "GET":
      print(f'it is GET request')
    elif request.method == "POST":
      nowtime = str(timezone.now())
      id = f'{request.user}--{nowtime[0:10:1]}_{nowtime[11:19:1]}'
      item_name = request.POST.get('item_name')
      item_price = request.POST.get('item_price')
      item_description = request.POST.get('item_description')
      product_id = id
      uploaded_files = request.FILES.getlist('images')  # Getting the uploaded images
      fields_json = request.POST.get('hidencollect')  # This is the JSON string
      print(f'{id}--{item_name}--{item_name}--{item_price}--{item_description}--{fields_json}--{uploaded_files}')

      if not uploaded_files:
        return render(request,'upload/upload_item.html',{'error':"please add minimum relevent imgage around 1:1"})
      print("is this json check ")
      print(f' type is -- {type(fields_json)}')
      try:
        item_others_details = json.loads(fields_json) if fields_json else {}
      except json.JSONDecodeError:
        print(f'it is not a json type is -- {type(fields_json)}')
        return render(request,'upload/upload_faill.html',{'user_data':handle_basic_request(request)})

      seller_instance = Seller.objects.get(user=request.user)

      item = seller_product.objects.create(
          user=seller_instance,
          item_name=item_name,
          price=item_price,
          product_id = product_id,
          description = item_description if item_description else "No description provided",
          item_others_details=item_others_details
        )
      print('product upload scessfull')

      product_code = f'img{product_id}'
      
      for i, image_file in enumerate(uploaded_files):
        img_id = f'{product_code}_{i}'
        print(f'image id is  -- {img_id}')
        i = i+1
        ItemImage.objects.create(related_product=item, image=image_file,image_id = img_id )

      print("images uplode sucessfill...")
      return render(request,'upload/upload_sucess.html')
      return render(request,'upload/upload_sucess.html',{'user_data':handle_basic_request(request),'product_items':json_data_for_homepage_products(request)})
    return render(request,'upload/upload_item.html',{'user_data':handle_basic_request(request)})
  except:
    return JsonResponse({'success': True, 'redirect_url': '/success/upload_sucess/'})


def collect_prodect_overview_data(request,product_id):
  print("yu are on the collect fields")
  over_product_data = seller_product.objects.filter(product_id = product_id)
  collected_data = {}
  for data in over_product_data:
    print(data)
    item_name = data.item_name
    item_others_details = data.item_others_details
    description = data.description
    price = data.price
    product_id = data.product_id
    collected_data = {'item_name':item_name,'product_id':product_id,'item_others_details':item_others_details,'description':description,'price':price}
  over_product_img = ItemImage.objects.filter(related_product__product_id = product_id)
  over_product_img = [img.image.url for img in over_product_img]
  collected_data={'collected_data':collected_data ,'over_product_img': over_product_img}
  print(f'collect data is :- {collected_data}')
  return collected_data
  
  # print(f'{collected_data}')

def product_Overview(request,product_id):
  print("now in product overview page ........")
  collect_prodect_overview_data(request,product_id)
  print(product_id)
  return render(request,'product_templates/product_Overview.html',{'collected_datas': collect_prodect_overview_data(request,product_id) ,'user_data':handle_basic_request(request)})

def upload_sucess(request):
  return render(request,'upload/upload_sucess.html')


@login_required
def cart(request):
  user = request.user
  print(user)
  allCart = cartItems.objects.filter(user = user)
  print(f'the cart data is --{allCart}')
  items_details = []
  for item in allCart:
    print(f'item is :- {item}')
    datafromdb = seller_product.objects.filter(product_id = item)
    for product in datafromdb:
      img = ItemImage.objects.filter(related_product = product)[0].image.url
      items_details.append({
          'name': product.item_name,
          'price': product.price,
          'image': img,
          'product_id': product.product_id
        })
  return render(request,'cart_templates/cart_.html',{'user_data':handle_basic_request(request),'cart_products' : items_details})


@login_required
def add_to_cart(request):
  if request.method == 'POST':
    try:
      # Parse the JSON data
      data = json.loads(request.body)
      productid = data.get('id')
      quantity = data.get('quantity')
      quantity = int(quantity)
      if not productid:
        return JsonResponse({'error': 'Product ID is required.','status':'400'}, status=400)
      print(f'the data is -- {data}')
      print(data.get('id'))
      user = request.user
      isAlreadyPresent = cartItems.objects.filter(user = user,productid = productid).exists()
      print(f'is this into db -- {isAlreadyPresent}')
      if isAlreadyPresent == False :
        cart_upload = cartItems.objects.create(user = user , productid = productid ,quantity = quantity)
        print(f'product is - {cart_upload}')
        return JsonResponse({'message': 'Item added to cart successfully.','status':'200'}, status=200)
      return JsonResponse({'message': 'Item already in to cart.','status':"201"}, status=201)

    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid JSON data.','status':False}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
  
def remove_from_cart(request):
  if request.method == 'POST':
    print("remove from cart")
    data = json.loads(request.body)
    product_id = data.get('id')  # Extract the actual product ID
    
    # Filter by the extracted product ID
    item_to_remove = cartItems.objects.filter(productid=product_id)
    
    if item_to_remove.exists():
      item_to_remove.delete()
      print("Item successfully removed.")
      return JsonResponse({'message': "Item is removed successfully", 'status': '200'})
    else:
      print("Item not found in the cart.")
      return JsonResponse({'message': "Item not found in cart", 'status': '201'})
  else:
    return JsonResponse({'message': "Invalid request method", 'status': '400'})
