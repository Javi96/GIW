# -*- coding: utf-8 -*-

# GIW - CURSO 17/18 - PRACTICA 8 - GRUPO 6
# AITOR CAYON RUANO
# JOSÉ JAVIER CORTÉS TEJADA
# FERNANDO PÉREZ GUTIÉRREZ
# GABRIEL SELLÉS SALVÀ

"""
Aitor Cayón Ruano, José Javier Cortés Tejada, Fernando Pérez Gutiérrez, Gabriel Sellés Salvà declaramos que esta solución
es fruto exclusivamente de nuestro trabajo personal. No hemos sido
ayudados por ninguna otra persona ni hemos obtenido la solución de
fuentes externas, y tampoco hemos compartido nuestra solución con
nadie. Declaramos además que no hemos realizado de manera deshonesta
ninguna otra actividad que pueda mejorar nuestros resultados
ni perjudicar los resultados de los demás.
"""

from mongoengine import StringField, IntField, FloatField, DateTimeField, ListField, EmbeddedDocument, ReferenceField, Document, EmbeddedDocumentField

from datetime import datetime, date

from mongoengine import ValidationError, connect

connect('giw_mongoengine') 

class Credit_Card(EmbeddedDocument):
    """ Clase que define la estructura de una tarjeta de crédito.
        
    :exception ValidationError: excepcion lanzada en caso de haber conflictos con el tipo de datos de 
    expiration_year, expiration_month, cvv o card_number
        
    .. note:: se han añadido un par de comparaciones extras además de las pedidas en el enunciado 
    para asegurar la integridad de los campos citados anteriormente
       

    """
    
    owner_name          = StringField(required = True)
    card_number         = StringField(required = True, min_length = 16, max_length = 16) 
    expiration_month    = StringField(required = True, min_length = 2,  max_length = 2) 
    expiration_year     = StringField(required = True, min_length = 2,  max_length = 2) 
    cvv                 = StringField(required = True, min_length = 3,  max_length = 3) 
    
    def clean(self):
        """ Metodo de validacion de la clase Credit_Card.
            
        :exception ValidationError: excepcion lanzada cuando:
            *card_number no es numerico
            *expiration_month no es numerico o no esta en el rango [1:12]
            *expiration_year no es numerico
            *cvv no es numerico
            
        .. note:: se han añadido un par de comparaciones extras además de las pedidas en el enunciado 
        para asegurar la integridad de los campos citados anteriormente
           
    
        """
        
        if(not self.card_number.isdigit()):
            raise ValidationError("El numero de la tarjeta de credito no está formado exclusivamente de dígitos.")
        if(not self.expiration_month.isdigit() ):
            raise ValidationError("El mes de caducidad no está formado exclusivamente de dígitos.")
        month= float(self.expiration_month) #Usamos float porque a veces int da fallos.
        if (month < 1 or month > 12):
            raise ValidationError("El mes de caducidad introducido no es valido (los posibles van del 1 al 12).")
        if(not self.expiration_year.isdigit() ):
            raise ValidationError("El año de caducidad no está formado exclusivamente de dígitos.")   
        if(not self.cvv.isdigit() ):
            raise ValidationError("El cvv no está formado exclusivamente de dígitos.")   
        
    
    
class Product(Document):
    """ Clase que define la estructura de un producto.
        
    :exception ValidationError: excepcion lanzada en caso de haber conflictos con el formato de los campos de la clase
        

    """
    
    barcode             = StringField(primary_key = True)
    name                = StringField(required = True)
    main_category       = IntField(required = True, min_value = 0)
    other_categories    = ListField(IntField(min_value = 0))
    
    def get_control_barcode_digit(self):
        """ Calcula y devuelve el digito de control del codigo de barras.
        
        :return: digito de control del codigo de barras
        
        ..note:: el algoritmo usado ha salido de esta fuente: http://www.grupoalquerque.es/mate_cerca/paneles_2012/166_Codigodebarras2.pdf.
        Hacemos conversiones a float dado que hemos tenido problemas al hacerlas a int
        
    
        """
        
        suma=0
        for x in range(0,12,1):
            if(x % 2==0):
                suma=suma+float(self.barcode[x])
            else:
                suma=suma+float(self.barcode[x])*3
        return 10-(suma % 10)
            
    def has_correct_barcode_format(self):
        """ Indica si el codigo de barras tiene el formato adecuado.
            
        :exception ValidationError: excepcion lanzada cuando:
            *barcode no es numerico, no esta formado por 13 elementos o el digito de control no es correcto
            
        :retorno: True si el codigo de barras esta bien formateado, False en otro caso
        
    
        """
        
        if(len(self.barcode)!=13 or not self.barcode.isdigit()):
            raise ValidationError("El codigo de barras no está compuesto correctamente.")
        if (self.get_control_barcode_digit()!=float(self.barcode[12])):
            raise ValidationError("El dígito de control del código de barras no encaja.")
        return True
    
    def clean(self):
        """ Metodo de validacion de la clase Product.
            
        :exception ValidationError: excepcion lanzada cuando:
            *barcode no tiene el formato correcto
            *main_category y el primer elemento de other_categories son distintos, siempre y
            cuando other_categories tenga al menos un elemento
                       
    
        """
        
        if(not self.has_correct_barcode_format()):
            raise ValidationError("El código de barras no está construido correctamente")
        if(len(self.other_categories)>0 and self.main_category!=self.other_categories[0]):
            raise ValidationError("No encajan las categorias.")
      
        

    
class Order_Line(EmbeddedDocument):
    """ Clase que define la estructura de las lineas de pedido.
            
    :exception ValidationError: excepcion lanzada en caso de haber incoherencias entre los datos de las instancias
       

    """
        
    ordered_products    = IntField(required = True, min_value = 1) 
    product_price       = FloatField(required = True, min_value = 0) 
    product_name        = StringField(required = True)
    total_price         = FloatField(required = True)
    product             = ReferenceField(Product, required = True)
    
    def clean(self):
        """ Metodo de validacion de la clase Order_LIne.
            
        :exception ValidationError: excepcion lanzada cuando:
            *el precio total difiere el calculado en base al numero de unidades y el precio individual
            *el nombre del producto y el de la linea de productos no encaja
            
        
        """
        if(self.total_price!=self.ordered_products*self.product_price):
            raise ValidationError("El valor total de una linea del pedido no encaja con el precio de la unidad * el numero de unidades")
        if(self.product_name!=self.product.name):
            raise ValidationError("El nombre del producto y el de la línea del producto no encajan.")

    
class Order(Document):
    """ Clase que define la estructura de los pedidos.
        
    :exception ValidationError: excepcion lanzada en caso de que haya incoherencias entre los campos de la clase
        

    """
        
    price   = FloatField(required = True)
    date_a  = StringField(required = True)
    lines   = ListField(EmbeddedDocumentField(Order_Line), required = True) 
    
    def get_order_price(self):
        """ Devuelve el precio total de la linea de productos
            
        :return: precio total de la linea de productos
           
    
        """
        
        result=0
        for x in self.lines:
            result=result+x.total_price
        return result
    
    def clean(self):
        """ Metodo de validacion de la clase Order.
            
        :exception ValidationError: excepcion lanzada cuando:
            *el precio total del pedido no concuerda con el calculado por get_order_price
                       
    
        """
        
        if(self.get_order_price()!=self.price):
            raise ValidationError("El valor total del pedido no encaja con la suma de las líneas que la componen.")
        
class User(Document):
    """ Clase que define la estructura de los usuarios.
        
    :exception ValidationError: excepcion lanzada cuando hay incoherencias en los campos de la clase
       

    """
        
    DNI                 = StringField(primary_key = True) 
    name                = StringField(required = True)
    first_surname       = StringField(required = True)
    second_surname      = StringField() 
    birthdate           = DateTimeField(required = True)
    last_accesses       = ListField(StringField(), max_length = 10)
    credit_cards_list   = ListField(EmbeddedDocumentField(Credit_Card)) 
    orders              = ListField(ReferenceField(Order, reverse_delete_rule = 4))    
       
    def has_correct_dni_format(self):
        """ Indica si el dni tiene un formato correcto.
            
        :exception ValidationError: excepcion lanzada cuando:
            *los 8 primeros digitos del campo dni no son numericos
            *la letra caldulada no concuerda con la del campo dni
        
        :return: True si el formato del campo dni es correcto, False en otro caso
                   
    
        """
        
        letters='TRWAGMYFPDXBNJZSQVHLCKE'
        number=self.DNI[0:8]
        if(not number.isdigit()):
            raise ValidationError("El DNI no está compuesto correctamente.")
        # De nuevo parseamos de string a float y luego a int
        number=float(number)
        number=int(number)
        number=number % 23
        if(self.DNI[8]!=letters[number]):
            raise ValidationError("El DNI no tiene el formato correcto.")
        
        return True
    
    def clean(self):
        """ Metodo de validacion de la clase User.
            
        :exception ValidationError: excepcion lanzada cuando:
            *el dni no tiene el formato correcto
                       
    
        """
        
        if(not self.has_correct_dni_format()):
            raise ValidationError("El DNI no tiene el formato correcto");

def insertar():
    """ Introduce en la base de datos los datos solicitado en el enunciado de la practica.


    """
    
    try:
        # productos
        p1 = Product(barcode = '5901234123457', main_category = 2, other_categories = [2,1,3], name = 'Nintendo Switch')
        p1.save()
        p2 = Product(barcode = '9002236311036', main_category = 1, other_categories = [1,8],   name = 'Toshiba X12A')
        p2.save()
        p3 = Product(barcode = '8412345678905', main_category = 3, other_categories = [],      name = 'Pan Bimbo')
        p3.save()
        p4 = Product(barcode = '9310779300005', main_category = 6, other_categories = [],      name = 'Bic Pen')
        p4.save()
        
        # líneas de pedido
        l1 = Order_Line(ordered_products = 1,  product_name = 'Nintendo Switch', product_price = 300, total_price = 300,  product = p1)
        l2 = Order_Line(ordered_products = 1,  product_name = 'Toshiba X12A',    product_price = 589, total_price = 589,  product = p2)
        l3 = Order_Line(ordered_products = 2,  product_name = 'Pan Bimbo',       product_price = 3,   total_price = 6,    product = p3)
        l4 = Order_Line(ordered_products = 5,  product_name = 'Bic Pen',         product_price = 2,   total_price = 10,   product = p4)
        l5 = Order_Line(ordered_products = 2,  product_name = 'Nintendo Switch', product_price = 300, total_price = 600,  product = p1)
        l6 = Order_Line(ordered_products = 2,  product_name = 'Toshiba X12A',    product_price = 589, total_price = 1178, product = p2)
        l7 = Order_Line(ordered_products = 5,  product_name = 'Pan Bimbo',       product_price = 3,   total_price = 15,   product = p3)
        l8 = Order_Line(ordered_products = 20, product_name = 'Bic Pen',         product_price = 2,   total_price = 40,   product = p4)
        
        # pedidos
        o1 = Order(price = 889,  date_a = '2017,12,12,16,50,12,1125', lines = [l1, l2])
        o1.save()
        o2 = Order(price = 16,   date_a = '2018,12,12,16,50,12,1125', lines = [l3, l4])
        o2.save()
        o3 = Order(price = 1778, date_a = '2019,12,12,16,50,12,1125', lines = [l5, l6])
        o3.save()
        o4 = Order(price = 55,   date_a = '2020,12,12,16,50,12,1125', lines = [l7, l8])
        o4.save()
        
        # tarjetas    
        cc1 = Credit_Card(owner_name = 'Juan Gomes Martirio', card_number = '1234567891234567', expiration_month = '05', expiration_year = '19', cvv = '100')
        cc2 = Credit_Card(owner_name = 'Juan Gomes Martirio', card_number = '9876543219876543', expiration_month = '06', expiration_year = '21', cvv = '200')
        cc3 = Credit_Card(owner_name = 'Juan Paga Bravas',    card_number = '5123156545456498', expiration_month = '07', expiration_year = '22', cvv = '300')
        cc4 = Credit_Card(owner_name = 'Juan Paga Bravas',    card_number = '2356489554126685', expiration_month = '08', expiration_year = '23', cvv = '400')
        
        # usuarios
        
        u1 = User(DNI = '43227700D', name = 'Juan', first_surname = 'Gomes', second_surname = 'Martirio', birthdate = '1996-5-3', 
                 last_accesses = ['2017,12,12,16,50,12,1125', '2015,12,05,16,40,12,1125'], credit_cards_list = [cc1, cc2], orders = [o1, o2])
        u1.save()
        u2 = User(DNI = '53472294P', name = 'Juan', first_surname = 'Paga',  second_surname = 'Bravas',   birthdate = '1992-6-3', 
                 last_accesses = ['2017,11,12,16,50,12,1125', '2015,06,05,16,40,12,1125'], credit_cards_list = [cc3, cc4], orders = [o3, o4])
        u2.save()
    except Exception as e:
        print('ERROR', e)

    # comandos para ver el contenido de la base de datos con la salida formateada
    # db.product.find().pretty()
    # db.order__line.find().pretty()
    # db.order.find().pretty()
    # db.credit__card.find().pretty()
    # db.user.find().pretty()