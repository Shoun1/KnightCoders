import requests
from django.http import HttpResponse
from django.shortcuts import render
from sklearn.naive_bayes import GaussianNB
#from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from admission.models import user
#from .forms import AdmissionForm
#from .serializers import userSerializer
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.feature_extraction.text import CountVectorizer
#from mlxtend.frequent_patterns import apriori,association_rules
# Create your views here.

'''class UserRegisterView(APIView):
    def get(self,request):
        # Fetch some data or simulate the registration data response
        form = AdmissionForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)

        return Response({"message": "Get method called successfully!"}, status=status.HTTP_200_OK)

    def post(self,request):
        #data = request.data
        u=Person()
        u.name = request.GET['name']
        u.email = request.GET['password']
        u.number = request.GET['number']
        u.password = request.GET['password']
        #fields = ["name","email","number","password"]
        #user = User(name=data['name'],
        #           email=data['email'],
        #           number=data['number'],
        #           password=data['password'])
        u.save()
        self.pull_data_from_api()
        return HttpResponse("Post successful")
        #serializer = UserSerializer(data=request.data)
        
        #if serializer.is_valid():
         #   serializer.save()
        #return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

def pull_data_from_api(self):
    try:
        url = "http://127.0.0.1:8000/api/user/register/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            #train_modelforstream(data)
            print(data)
            return HttpResponse(f"Data received: {data}")
        else:
            return HttpResponse('Error inr retrieving the data')
    except requests.exception.RequestException as e:
        print(f"Error occurred while making the request: {e}")
        return HttpResponse(f"Error occurred: {e}")'''

def admissionpage(request):
    return render(request,'form.html')

def admissioncode(request):
    u=user()
    u.name = request.GET['name']
    print(u.name)
    u.fathername=request.GET['fathersName']
    u.mothername=request.GET['mothersName']
    u.email = request.GET['email']
    u.phone = request.GET['phone']
    u.jee_marks = request.GET['jee_marks']
    u.city=request.GET['city']
    u.country=request.GET['country']
    u.state=request.GET['state']
    #print(f"Name: {u.name}")
    #print(f"Father Name: {u.fathername}, Email: {u.email}, etc.")
    u.save()
    context = {
        'name': u.name,
        'fathers name': u.fathername,
        'mothers name': u.mothername,
        'email': u.email,
        'number': u.number,
        'jee_marks': u.jee_marks,
        'country': u.country,
        'state': u.state,
        'city': u.city
    }
    return render(request,'form.html',context)

def train_modelforstream(data):
    #data = np.array([140,142,152,184,147,120,721,561,418,412]).reshape(-1,1)
    X_train = np.array([382,994,982,47,521,459,205,558,314,218]).reshape(-1,1)
    X_test = np.array([507,818,452,368,242,846,825,615,583,607])
    Y_train = np.array([1,0,1,0,0,1,0,1,0,1])
    Y_test = np.array([1,1,1,1,1,0,0,1,0,0])
    model = GaussianNB()
    model.fit(X_train,Y_train)
    data = np.array([140,142,152,184,147,120,721,561,418,412]).reshape(-1,1)
    #X_test = data.iloc[:].reshape(-1,1)
    X_test = data
    pred = model.predict(X_test)
    chances = []
    u = user.objects.all()
    st_ids = u.values_list('id',flat=True)
    student_ids=[]
    for val in pred:
        chances.append(val)
    for id in st_ids:
        student_ids.append(id)
    eligibility ={'id':student_ids,'chances':chances}
    print(eligibility)
    #return render(request,'results.html',{'eligiblity':eligibility})

u = user()
st = user.objects.all()
marks = np.array(st.values('jee_marks'))
train_modelforstream(marks)

'''def train_modelfordoc():
    doc = documents.values('documents','location')
    X_train = np.empty((len(doc),1),dtype=object)
    Y_train = np.empty((len(doc),1),dtype=int)
    for i,text in enumerate(doc):
        X_train[i] = text['documents']
        Y_train[i] = text['location']

    return X_train,Y_train
    X_train_list=[]
    Y_train_list=[]

    for text in doc:
        X_train_list.append(text['documents'])
        Y_train_list.append(text['location'])
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_train_list)

    X_train = np.array(X_train_list)
    Y_train = np.array(Y_train_list)

    return X_train,Y_train

def make_predictionsfordoc(request):
    X_train,Y_train = train_modelfordoc()
    model = MultinomialNB()
    model.fit(X_train,Y_train)
    X_test = vectorizer.transform(data.iloc[:].reshape(-1,1))
    doc_pred = model.predict(X_test)
    return render(request,'.html'.{'doc_pred':doc_pred})

def predict_nextfield(data,input_fields):
    one_hot_data  = pd.get_dummies(data)
    #generate frequent item-sets
    frequent_itemsets = apriori(oen_hot_data,min_support=0.1,use_colnames=True)
    #generate association rules
    rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.5)

    predictions=set()
    for __rule in rules.iterrows():
        antededents = set(rule['antecedents'])
        consequents = set(rule['conseqquents'])

        #if users selection matches the antecedents
        is users_selection.issubset(antecedents):
            predictions.update(consequents)
    
    return redirect('../dynamic_view/<predictions>')

class DynamicForm(forms.Form):

    def __init__(self,*args,**kwargs):
        pred_fields = kwargs.pop('pred_fields',[])
        super().__init__(*args,**kwargs)
        for field in pred_fields:
            #add a CharField to the form
            self.fields[field] = forms.CharField(labels=field.capitalize(),
                                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                                required=False)
    

    def dynamic_view(request,predictions):

        if request.method == 'POST':
            form = DynamicForm(request.POST,pred_fields=predictions)
            if form.isvalid():
                print(form.cleaned_data)
                return render(request,'success.html',{'data':cleaned_data})
            else:
                #instantiate form with dynamic fields
                form = DynamicForm(pred_fields=predictions)
            
                return render(request,'form.html',{'form':form,'predictions':predictions}) 


train_modelforstream()
make_predictionsfordoc()


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # This will raise an IntegrityError if the username already exists
                messages.success(request, 'Account created successfully!')
                return redirect('userauth:login')
            except IntegrityError:
                messages.error(request, 'An error occurred. Username might already exist.')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors below.')
            # Log form errors for debugging
            for field in form:
                for error in field.errors:
                    print(f'Error in {field.name}: {error}')
            print(form.errors)  # This will print all errors to the console
    else:
        form = CustomUserCreationForm()

    return render(request, '/register.html', {'form': form})'''
