from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from clients.models import clientrequirement
# Create your views here.
def carbonpage(request):
    return render(request,"carbon/carbonhome.html")


def carbonregistration(request):
    if request.method=="POST":
        name=request.POST['name']
        emailid=request.POST['emailid']
        address=request.POST['address']
        phoneNo=request.POST['phoneno']
        password=request.POST['password']
        try:
           carbonregister(name=name,emailid=emailid,address=address,phoneno=phoneNo,password=password).save()
           messages.success(request, " carbonFiber team registered successfully")
           return render(request,"carbon/carbonlogin.html")
        except:
           messages.info(request," carbonFiber team not registered successfully")
           return render(request, "carbon/carbonregister.html")

    return render(request,"carbon/carbonregister.html")


def carbonlogin(request):
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        password = request.POST.get('password')

        try:
            carbon = carbonregister.objects.get(emailid=emailid, password=password)

            if carbon.approve:
                messages.info(request, "carbonfiber Login Successful")
                request.session['user_id'] = carbon.id
                print( request.session['user_id'])
                carbon.login = True
                carbon.logout = False
                carbon.save()
                return redirect("/carbonhome/")
            else:
                messages.info(request, "carbonfiber team need management approval to access")
                return render(request,"carbon/carbonlogin.html")

        except carbonregister.DoesNotExist:
            messages.info(request, " carbonfiber team enter Invalid Email or Password")

    return render(request,"carbon/carbonlogin.html")

def carbonlogout(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        try:
            carbon = carbonregister.objects.get(id=user_id)
            carbon.logout = True
            carbon.login = False
            carbon.save()
            del request.session['user_id']
            return redirect('/mainpg/')
        except carbonregister.DoesNotExist:
            request.session.pop('user_id', None)
            messages.error(request, 'team not found')
    else:
        messages.info(request, 'You are already logged out')

    return redirect('/mainpg/')


def viewcltcarbonreq(request):
    viewall1 = clientrequirement.objects.values_list('clientid','orderid','catagory').distinct().filter(catagory="carbonFiber")
    print('viewall:', viewall1)
    client_id = [each[0] for each in viewall1]
    print('dta1: ', client_id)
    return render(request, 'carbon/viewcltcarbonreq.html',  {'data': viewall1,'client_id':client_id})


def viewcltcarbondataset(request, clientid):
    viewall=clientrequirement.objects.filter(clientid=clientid,catagory="carbonFiber")
    return render(request, 'carbon/viewcltcarbondata.html',{'viewall': viewall})

import pandas as pd
from pandas.errors import ParserError, EmptyDataError
import random


def carbonuploaddataset(request):

    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['carbondataset']
            data = pd.read_csv(uploaded_file)
            for index, row in data.iterrows():
                 instance = carbondataset(
                 mProduct=row['mProduct'],
                 Netcontent=row['Netcontent'],
                 Netweight=row['Netweight'],
                 manufactureprocess=row['manufactureprocess'],
                 RawMaterials=row['RawMaterials'],
                 Recyclingprocess=row['Recyclingprocess'],
                 ).save()
            messages.success(request, "carbon fiber reinforcement Dataset uploaded successfully")
            return redirect('/carbonhome/')
        except ParserError as e:
                    messages.error(request, f"Error parsing the CSV file: {e}")
        except EmptyDataError as e:
                    messages.error(request, f"The CSV file is empty: {e}")
        except Exception as e:
                    messages.error(request, f"An error occurred: {e}")
    return render(request, "carbon/carbonuploaddata.html")


def carbonprocessdataset(request):
    viewall1 = clientrequirement.objects.values_list('clientid', 'orderid', 'catagory','MProcess').distinct().filter(catagory="carbonFiber")
    client_id = [each[0] for each in viewall1]
    orderid = [each[1] for each in viewall1]
    return render(request, 'carbon/carbonanalysedata.html', {'data': viewall1, 'client_id': client_id,'orderid':orderid })

def carbonanalysedataset(request,orderid):
        client_products = clientrequirement.objects.filter(orderid=orderid,catagory="carbonFiber")


from sklearn.neighbors import KNeighborsRegressor
from django.shortcuts import redirect
from django.http import HttpResponse
def carbonprocessing(request, orderid):
    # Fetch client products and quantities from the database based on the orderid and category
    client_products = clientrequirement.objects.filter(orderid=orderid, catagory="carbonFiber")
    products = [
        "Carbon Fiber Rovings",
        "Carbon Fiber Chopped Strands",
        "Carbon Fiber Nonwovens",
        "Carbon Fiber Mat",
        "Carbon Fiber Tow",
        "Carbon Fiber Braided Sleeves",
        "Carbon Fiber Chopped Mat",
        "Carbon Fiber Felt"
    ]

    net_content = [0.6, 0.5, 0.7, 0.6, 0.85, 0.7, 0.4, 0.5]
    net_weight = [0.3, 0.2, 0.3, 0.4, 0.1, 0.6, 0.5, 0.3]

    # Calculating ghost fishing nets quantity (kg) for each product
    ghost_fishing_nets_quantity = [net_content[i] * net_weight[i] for i in range(len(products))]

    # Client dataset with quantities (retrieved dynamically from the database)
    unknown_products = []
    client_quantities = []
    unknown_net_content = []  # Initialize lists for unknown product data
    unknown_net_weight = []

    for product in client_products:
        unknown_products.append(product.mProduct)
        # Assuming the product name field in the model is 'product_name'
        client_quantities.append(product.quantity)  # Assuming the quantity field in the model is 'quantity'
        # Fetch net content and net weight for each product from the database
        # Assuming you have fields 'net_content' and 'net_weight' in your model
        if product.mProduct in products:
            index = products.index(product.mProduct)
            print(index)
            unknown_net_content.append(net_content[index])
            unknown_net_weight.append(net_weight[index])
    # Reshape the data for KNN input
    X = [[quantity] for quantity in ghost_fishing_nets_quantity]
    # Fit KNN model
    knn = KNeighborsRegressor(n_neighbors=3)  # You can adjust the number of neighbors as needed
    knn.fit(X, client_quantities)

    # Calculate ghost fishing nets quantity for unknown products
    unknown_ghost_fishing_nets_quantity = [unknown_net_content[i] * unknown_net_weight[i] for i in range(len(unknown_products))]
    print(unknown_ghost_fishing_nets_quantity)
    # Predict quantities using KNN model
    predicted_quantities = knn.predict([[quantity] for quantity in unknown_ghost_fishing_nets_quantity])
    product_predicted_quantities = dict(zip(unknown_products, predicted_quantities))
    for result in predicted_quantities:
        print('result:',result)
    predict_quantities_List= predicted_quantities
    print('predicted_quantities:',type(predicted_quantities))
    print('predicted_quantities:', predicted_quantities)
    # Display predicted quantities for unknown products
    for i in range(len(unknown_products)):
        print(f"Predicted quantity for {unknown_products[i]}: {predicted_quantities[i]}")
        print('unknown_products:::::: ',unknown_products[i])
        print(predicted_quantities[i])
        # Update clientrequirement object with mechregister data
        for client_product in client_products:
            cltproduct = client_product.mProduct
            try:
                datas = carbondataset.objects.filter(mProduct=cltproduct)
                for data in datas:
                  client_product.Netcontent = data.Netcontent
                  client_product.Netweight = data.Netweight
                  client_product.manufactureprocess = data.manufactureprocess
                  client_product.RawMaterials = data.RawMaterials
                  client_product.Recyclingprocess = data.Recyclingprocess
                  client_product.ghostfishingnets = product_predicted_quantities.get(client_product.mProduct, 0.0)
                  client_product.MProcess = True
                  client_product.save()

            except carbondataset.DoesNotExist:
                # Handle case where mechregister object doesn't exist for the given mProduct
                # You may want to redirect or display an error message
                pass
    messages.success(request, 'Carbon fiber reinforcements processed successfully')
    return redirect('/carbonhome/')



def carbonreport(request):
    viewall1 = clientrequirement.objects.values_list('clientid', 'orderid', 'catagory','MProcess','mechreport').distinct().filter(
        catagory="carbonFiber",MProcess=True)
    client_id = [each[0] for each in viewall1]
    return render(request,'carbon/carbonreport.html',{'data': viewall1, 'client_id': client_id})


def viewcarbonreport(request,clientid):
    viewall=clientrequirement.objects.filter(clientid=clientid,catagory="carbonFiber",MProcess=True)
    return render(request, 'carbon/viewcarbonreport.html',{'data': viewall})


def sendcarbonreport(request,clientid):
    viewall=clientrequirement.objects.filter(clientid=clientid,catagory="carbonFiber",MProcess=True)
    for client_product in viewall:
        client_product.mechreport = True
        client_product.save()
    messages.success(request, "carbonfiber reinforcements report send to admin successfully")
    return redirect("/carbonhome/")





