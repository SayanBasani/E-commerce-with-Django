from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import check_password,make_password
from .models import Seller,UserProfile,CustomUser
# from django.contrib import sessions
# Create your views here.


def user_singup(request):
  print(request.method)
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    print(f'{username}--{email}--{first_name}--{last_name}--{password}')
    if CustomUser.objects.filter(username=username).exists():
        return render(request, 'users_singup.html', {'message': 'This username is already taken', 'email': email, 'first_name': first_name, 'last_name': last_name})
    if CustomUser.objects.filter(email=email).exists():
        return render(request, 'users_singup.html', {'message': 'This email is already used', 'username': username, 'first_name': first_name, 'last_name': last_name})
    # Create the user
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    print(user)
    print(user.password)
    user.role = CustomUser.Role.USER
    user.save()
    print("User created in User DB successfully...")
    # Check if UserProfile already exists
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    if created:
      print("UserProfile created in UserProfile DB successfully...")
    else:
      print("UserProfile already exists for this user.")

    print("User singup successful...")
    login(request, user)
    print("User is successfully logged in...")
    return redirect('shop:home')
  return render(request, 'users_singup.html')


def seller_singup(request):
  print(request)
  print(request.method)
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    seller_status = "Y"

    print(f'{username}--{email}--{first_name}--{last_name}--{password}')

    if CustomUser.objects.filter(username = username ).exists():
      return render(request,'users_singup.html',{'massage':'this user name already taken','email':email,'first_name':first_name,'last_name':last_name,'password':password})

    if CustomUser.objects.filter(email = email ).exists():
      return render(request,'users_singup.html',{'massage':'this email already used','username':username,'first_name':first_name,'last_name':last_name,'password':password})
    # try :  
    if username and email and first_name and last_name and password:
      user = CustomUser.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password = password
      )
      user.role = CustomUser.Role.SELLER
      user.save()
      # user_profile, created = UserProfile.objects.get_or_create(user=user)
      seller_profile, created = Seller.objects.get_or_create(user = user , defaults = { 'seller_status':seller_status})
      if created:
        print("UserProfile created in UserProfile DB successfully...")
      else:
        print("UserProfile already exists for this user.")

      print("User singup successful...")
      login(request, user)
      print("User is successfully logged in...")
      return redirect('shop:home')
    else:
      return render (request,'seller_singup.html')
  return render(request,'seller_singup.html')
 

def user_login(request):
  print(request.path)
  return _login(request)

def seller_login(request):
  return _login(request)


def _login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    # print(f'Username: {username}, Password: {password}')  # Add this for debugging
    user = authenticate(request, username=username, password=password)
    # print(user.get_role_display())
    if user is not None:
      login(request, user)
      user_data = {
        'username':user.username,
        'role' : user.Role
      }
      print(user_data)  #.get_role_display()
      print("User is successfully logged in...")
      return redirect('shop:home')
    else:
        # Show an error message if authentication fails
        return render(request, 'login.html', {'error': 'Invalid username or password'})
  return render(request, 'login.html')


def _logout(request):
  logout(request)
  return redirect('account:user_login')





# def seller_login(request):
#   if request.method == 'POST':
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request,username = username , password = password)
#     if user is not None and isinstance(user,seller_models):
#       login(request,user)
#   return render(request,'login.html')


# def user_login(request):
#   if request.method == 'POST':
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request,username = username , password = password)
#     if user is not None and isinstance(user,User):
#       login(request,user)
#   return render(request,'login.html')



# def seller_singup(request):
#   if request.method == 'POST':
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     password = request.POST.get('password')
#     if seller_models.objects.filter(username = username ).exists():
#       return render(request,'singup.html',{'massage':'this user name already taken','email':email,'first_name':first_name,'last_name':last_name,'password':password})
#     if seller_models.objects.filter(email = email ).exists():
#       return render(request,'singup.html',{'massage':'this email already used','username':username,'first_name':first_name,'last_name':last_name,'password':password})
#     user = seller_models.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
#     user.save()
#     login(request,user)
#     return render(request,'home.html')
#   return render(request,'singup.html')

# def seller_login(request):
#   return _login(request,seller_models)



# def user_singup(request):
#   if request.method == 'POST':
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     password = request.POST.get('password')
#     if User.objects.filter(username = username ).exists():
#       return render(request,'singup.html',{'massage':'this user name already taken','email':email,'first_name':first_name,'last_name':last_name,'password':password})
#     if User.objects.filter(email = email ).exists():
#       return render(request,'singup.html',{'massage':'this email already used','username':username,'first_name':first_name,'last_name':last_name,'password':password})
#     user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
#     user.save()
#     login(request,user)
#     return render(request,'home.html')
#   return render(request,'singup.html')
