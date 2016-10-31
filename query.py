"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
q1 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
q2 = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()
# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year<1960).all()
# Get all brands that were founded after 1920.
q4 = Model.query.filter(Model.year<1960).all()
# Get all models with names that begin with "Cor".
q5 = Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None ).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued.isnot(None))).all()
# Get all models whose brand_name is not Chevrolet.
q8 = Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    model_list = Model.query.filter_by(year=year).all()
    for model in model_list:
        print 'The Model is %s, its brand name is : %s and the headquarters are in %s'%(model, model.brand_name, model.brand.headquarters)
    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    model_list = Model.query.order_by(Model.brand_name).all()
    temp_brand = model_list[0].brand_name
    for model in model_list:
        # print 'The brand name is %s and its models are:'%(brand.name)
        if temp_brand == model.brand_name:
            print '- ' + model.name
        else:   
            print '\n' + model.brand_name
            print '- ' + model.name 
        temp_brand = model.brand_name 

# I realize that this is not optimal because the model is repeated multiple times. 
# I was not able to 'group_by' model so we keep one unique model name.
 # Another idea I had was to use 'join'. I tried but was not successful. My idea was:
 # q1 = db.session.query(Brand.name, Model.name).outerjoin(Model).group_by(Model.name).order_by(Brand.name, Model.name)
# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# The return value is <flask_sqlalchemy.BaseQuery object at 0x7f0a2a44f650> which 
# is a Query object inheriting from SQLAlchemy class. To obtain a result from this 
# Query it is needed to fetch it as followed: Brand.query.filter_by(name='Ford').all()
# By doing that we will obtain all 'Brand object' from the brands table that meet 
# the criteria.
# Brand.query.filter_by(name='Ford').all() is a list of Brand. 

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# When a many to many relationship exists between two tables but there is no common 
# key that linked both tables (the way we had in the previous excercise:
 # the name of the brand was the link  between our brands and models table, and was 
# present in both), association table are created to create this 'artifical link' 
# between both tables. It usually includes the primary key of both tables and its own 
# primary key.
# Example of many to many relationship => user table and password table: a user can
# have multiple different passwords depending on the website he/she is using. 
# Passwords can be shared by multiple users.
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    return Brand.query.filter(Brand.name.like('%Chev%')).all()


def get_models_between(start_year, end_year):
    return Brand.query.filter(Brand.founded>=1928,Brand.discontinued<2002).all()
