# !/usr/bin/env python
# -*- coding: utf-8 -*-
#import ply.lex as lex 
#import pandas as pd
import sys
import re
import csv
#import lista

class Nodo:
    def __init__(self,dato,tokem,line_):
        self.cmd= dato
        self.token=tokem
        self.line=line_
        self.siguiente = None
    def __str__(self):
    	return " cm:%s\n token:%s\n line:%i" % (self.cmd,self.token,self.line)

class Lista:

    def __init__(self):
        self.cabeza = None
        self.tail = None
        self.cont = 0;
    def insertar(self,cmd,token,line):
    	tmp=Nodo(cmd,token,line)
    	if self.cabeza==None:#si la cabeza esta vacia
    	    self.cabeza=tmp
    	if self.tail!=None:
    	    self.tail.siguiente=tmp

    	self.tail=tmp 
    	self.cont=self.cont+1;
    	 

    def imprimir_lista(self):
         actual=self.cabeza
         while actual!=None :
                print(actual)
                print(' 			\n')
                actual=actual.siguiente;
    def size(self):
    	return self.cont;
    	
class Pila:
     def __init__(self):
         self.items = []

     def Empty(self):
         return self.items == []

     def Push(self, item):
         self.items.append(item)

     def Pop(self):
         return self.items.pop()

     def Top(self):
         return self.items[len(self.items)-1]

     def Len(self):
         return len(self.items)
     def Print(self):
         stringtmp="["
         for i in self.items:
             stringtmp=stringtmp+i+" "
         stringtmp=stringtmp+"]"
         print(stringtmp)



#tokens
#
def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL) ,"",string) # remueve los comentarios de varias filas (/*COMMENT */)
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remueve todos los comentarios de una sola linea (//COMMENT\n )
    if (re.compile("//*.*"), "", string):
        string = re.sub(re.compile("//*.*"), "#@", string)
        #print("cadena: "+string)
    return string

# Diccionario Tokens
# -----------------------------------------------------------------------------
tknIdentificador = re.compile('[a-zA-Z0-9]+$')
tknNumero=re.compile('[0-9]+')

exp_ID = re.compile('[a-zA-Z]+[a-zA-Z1-9/_]*')
exp_str= re.compile('"[a-zA-Z0-9]+"')
exp_Int = re.compile('[0-9]+')
exp_Float = re.compile('[0-9]+.[0-9]+')
op_arti = 'OP_aritmetica'


# Autómatas
#-----------------------------------------------------------------------------
def  tokens(temp):
        
        if temp == "create" or temp=="CREATE": #create
            return 'PR_create'
        elif temp == "select" or temp=="SELECT":  #select
            return 'PR_select'
        elif temp == "insert" or temp=="INSERT":   #Insert
            return 'PR_insert'
        elif temp == "update" or temp=="UPDATE":    #update 
            return 'PR_update'
        elif temp == "delete"or temp=="DELETE":    #delete
            return 'PR_delete'
        elif temp == "from" or temp=="FROM":       # from 
            return 'PR_from'
        elif temp == "table" or temp=="TABLE":       # TABLE 
            return 'PR_table'
        elif temp == "where" or temp =="WHERE":    #where
            return 'PR_where'
        elif temp == "into" or temp=="INTO":
            return 'PR_into'
        elif temp == "set" or temp=="SET":
            return 'PR_set'
        elif temp == "values" or temp=="VALUES":
            return 'value'
        #operacion de agrupamiento 
        elif temp == "(":
            return "tkn_parentesis_abierto"
        elif temp == ")":
            return "tkn_parentesis_cerrado"
        #operacionde puntuacion
    	elif temp == ".":
            return "tkn_punto"
        elif temp == ",":
            return "tkn_coma"
        elif temp == ";":
            return "tkn_puntoComa"
        elif temp == ":":        #----------------------de asignacion 
            return "tkn_dosPuntos"
        elif temp == "==" :
        	return "tkn_igual_igual"
        
        #operacion aritmetica

        elif temp == "+":
        	return "oper_s"
        elif temp == "-":
            return "oper_r"
        elif temp == "*" :
        	return "oper_m"
        elif temp == "/":
            #return op_arti
            return "oper_d"

        #noTerminales={'PR_select','PR_insert','PR_update','PR_delete','PR_num','tkn_str','tkn_id','pr_count','pr_max','pr_min','pr_avg','pr_sum','tkn_AND','tkn_OR','tkn_NOT','OP_booleano'}
        
        #tipo de variable 
    	elif temp == "register" or temp == "REGISTER" :
    		return "PR_register"
        elif temp == "auto" or temp == "AUTO":
            return "PR_funtionAuto"
        elif temp == "random" or temp == "RANDOM":
            return "PR_funtionRandom"
        #tipo de variable 
        elif temp == "varchar" or temp == "VARCHAR":
            return "PR_varchar"
        elif temp == "int" or temp == "INT":
            return "PR_entero"
        elif temp == "$":
            return "$"


        elif re.match(exp_ID, temp):
            m = re.match(exp_ID, temp)
            #print m;
            if len(m.group(0)) == len(temp):
            #    print ('m:     '+m.group(0));

                return "tkn_id"
        elif re.match(exp_str, temp):
            m = re.match(exp_str, temp)
            #print m;
            if len(m.group(0)) == len(temp):
            #    print ('m:     '+m.group(0));

                return "tkn_str"

        elif re.match(exp_Int, temp): #evaluar exp reg
                m = re.match(exp_Int, temp)
                if len(m.group(0)) == len(temp):
	                return "PR_num"
	                print ('m:     '+m.group(0));
		"""elif re.match(exp_Float, temp): #evaluar exp reg
				m = re.match(exp_Float, temp)
				if len(m.group(0)) == len(temp):
					return "PR_num"
	                #print ('m:     '+m.group(0));"""
        else:
            return "PR_Undefined"
         
# pocesamiento
#-----------------------------------------------------------------------------
def data_list_reglon(data):
	lista = []
	for renglon in data:
	    noCommetns = removeComments(renglon)
	    lista.append(noCommetns)
	return lista
 
# Preprocesamiento
#-----------------------------------------------------------------------------
"""file = open('codigo.txt', 'r')
data = file.readlines()
file.close() """

def procesamiento(lista):
    linea = 0
    contador=0
    aux=""
    file = open('codigo.txt', 'r')
    data = file.readlines()
    for renglon in data:
        noCommetns = removeComments(renglon)
        linea = linea + 1
        if noCommetns!="\n":# cuando el reglon es diferente de vacio
        	noCommetns=noCommetns+' $'
        	#print("sin comentario: "+noCommetns)
        	for palabra in  noCommetns.split(' '):
        #    if palabra == "":
        #        continue

				aux=tokens(palabra)
				if aux==None or aux=="PR_Undefined":
					#print("hi->"+palabra+"-----------")
					#t=tokens(palabra)
					#l2="   l: "+str(linea)
					#print("tkn"+t)
					#print(l2)
					#print("pala:->"+palabra+"<-")
					subpalabras=list(filter(None, re.split(r"([+]|-|[*]|[/]|;|,|[.]|[:]|==|=|<=|>=|<|>|[(]|[)]|[[]|[]]|{|}|[\r])", palabra)))
		            #se sacan las subpalabras que pueden haber ejem. 2+4 -> 2 + 
					for delimitadores in subpalabras:
						#print("d->|"+delimitadores+"|")

						if(delimitadores == "#@"):
							print ("Error de comentario en la Linea: ",linea)
							break
						if(delimitadores != ('\n')):
							if (delimitadores != ('\r')):
								token_s=tokens(delimitadores)
								lista.insertar(delimitadores,token_s,linea)
				else:
					tkn=tokens(palabra)
					lista.insertar(palabra,tkn,linea)
					#li="->"+palabra+"  l: "+str(linea)
					#print(li)
	file.close()

        
        #linea = linea + 1
def checkfile(archivo):
	import os.path
	if os.path.exists(archivo):
		return True;
	else:
		return False;
def randome(a,b):
	import random
	return a+random.randrange(b)

def funRegister(nameFile,cantidad):
	t=[]
	r=[]
	aux=[]
	cantid=int(cantidad)
	cantid=cantid+1
	cant=1
	file = open(nameFile, 'r')
	data = file.readlines()
	aux=data[0]
	#r.append(aux)
	tmp=[]
	for renglon in aux.split(","):
		tmp.append(renglon)
		if(renglon!="\n"):
			subpalabras=list(filter(None, re.split(r"([:]|[(:]|[):])",renglon)))
			t.append(subpalabras)
	r.append(tmp)
	while cant<cantid:
		#print(str(cant))
		l=[]
		for i in range(0,len(t)):
			#print(t[i])
			if(t[i][2]=='int' and t[i][4]=='auto'):
				l.append(cant)
			elif(t[i][2]=='int' and t[i][4]=='random'):
				l.append(randome(int(t[i][6]),int(t[i][8])))
			elif(t[i][2]=='varchar' or t[i][2]=='VARCHAR' ):
				l.append(t[i][0]+"_"+str(cant))
		cant=cant+1
		r.append(l)
	file.close()
	print(r)
	output=open(nameFile,"w")
	filOut=csv.writer(output)
	for row in r:
		filOut.writerow(row)
	output.close()


def showFile(nameFile):
	if(checkfile(nameFile)==True):
		file = open(nameFile, 'r')
		data = file.readlines()
		for row in data:
			strT="		"
			for colm in row.split(","):
				strT=strT+ colm+"   "
			print(strT) 

	else:
		print(" no existe la tabla "+nameFile)
def showFileCondition(cond1,oper,cond2,nameFile):
		t=[]
		indexC1=0
		indexC2=0
		l=[]
		print(nameFile)
	#if(checkfile(nameFile)==True):
		file = open(nameFile, 'r')
		data = file.readlines()
		for renglon in data[0].split(","):
			if(renglon!="\n"):
				subpalabras=list(filter(None, re.split(r"([:]|[(:]|[):])",renglon)))
				t.append(subpalabras)
		for i in range(0,len(t)):
			if(t[i][0]==cond1):
				indexC1=i
		print("condicion "+ str(indexC1))
		for i in range(1,len(data)):
			m=list(filter(None, re.split(r"([,]|[\n]|[\r])",data[i])))
			print(m)
			for j in range(0,len(m)):
				if(j==indexC1 +indexC1):
					if(m[j]==cond2):
						l.append(data[i])
		#print(l)
		for row in l:
			strT="		"
			for colm in row.split(","):
				strT=strT+ colm+"   "
			print(strT) 

	#else:
		#print(" ...no existe la tabla  selectionada "+nameFile)
def deleteRegister(cond1,cond2,nameFile):
		t=[]
		indexC1=0
		indexC2=0
		l=[]
		print(nameFile)
	#if(checkfile(nameFile)==True):
		file = open(nameFile, 'r')
		data = file.readlines()
		tmp=[]
		for renglon in data[0].split(","):
			tmp.append(renglon)
			if(renglon!="\n"):
				subpalabras=list(filter(None, re.split(r"([:]|[(:]|[):])",renglon)))
				t.append(subpalabras)
		for i in range(0,len(t)):
			if(t[i][0]==cond1):
				indexC1=i
		#print("condicion "+ str(indexC1))
		l.append(tmp)
		for i in range(1,len(data)):
			for reglon in data[i].split(","):
				if(reglon!="\n"):
					m=list(filter(None, re.split(r"([\n]|[\r])",data[i])))
					for j in range(0,len(m)):
						if(j==indexC1):
							if(m[j]!=cond2):
							   #filOut.writerow(data[i])
							   l.append(m)
		output=open(nameFile,"w")
		filOut=csv.writer(output)
		filOut.writerow(tmp)
		for row in l:
			#print(row)
			t=[]
			for colm in range(0,len(row)-2):
				t=[]
				for i in row[colm].split(","):
					t.append(i)
				filOut.writerow(t)

		output.close()		

				


				
		"""output=open(nameFile,"w")
		filOut=csv.writer(output)
		for row in l:
			print(row)
			filOut.writerow(row)
		output.close()"""
		 





#**************ANALIZADOR SINTACTICO******************
def AnalizadorSintactico(listaTokens):#listatokens.imprimir_lista()
    	tama=listaTokens.size()
    	tmp=listaTokens.cabeza
    	SimbActual=tmp.token
    	print("esterminal " + SimbActual)
    	listaTokens.imprimir_lista();

    	while(SimbActual!='$'):
    		#print("size "+str(tama))
    		listCampos = []
    		if(SimbActual=="PR_create"):
    			tmp=tmp.siguiente
    			SimbActual=tmp.token
    			if(SimbActual=="PR_table"):# crearemos una tabla
    				print("creando archivo")
    				tmp=tmp.siguiente
    				SimbActual=tmp.token
    				nameFile=tmp.cmd+".csv" #nombre de la tabla
    				tmp=tmp.siguiente   #debe ser parentesis
    				SimbActual=tmp.token
    				cont=0;
    				if (SimbActual=="tkn_parentesis_abierto"):
    					cont+=1;
    				#print("hey ."+SimbActual)
    				while (cont>0):
    					t = ""
    					tmp=tmp.siguiente
	    				SimbActual=tmp.token
	    				if(SimbActual=="tkn_id"):
	    					while (SimbActual!="tkn_coma" and cont>0):
		    					t=t+tmp.cmd  #capturando el tkn_id
		    					tmp=tmp.siguiente
		    					SimbActual=tmp.token
		    					if(SimbActual=="tkn_parentesis_abierto"):
		    						cont=cont+1
		    					if(SimbActual=="tkn_parentesis_cerrado"):
		    						cont=cont-1
	    				print(t)
	    				listCampos.append(t)
	    	
    				#creando el archivo
    				archivo=open(nameFile,"w")
	    			for i in listCampos:
	    				archivo.write(i+",")
	    			archivo.write("\n")
    				archivo.close()
    			else:
    				print("error in linea "+tmp.line);
    		elif(SimbActual == "PR_select"):
    			tmp=tmp.siguiente
    			SimbActual=tmp.token
    			if (SimbActual=="oper_m"):
    				tmp=tmp.siguiente #palabra  from
    				tmp=tmp.siguiente  #nombre de la tabla
    				nameFile=tmp.cmd+".csv" 
    				tmp=tmp.siguiente
    				SimbActual=tmp.token
    				if(SimbActual=="PR_where"):
    					tmp=tmp.siguiente
    					cond1=tmp.cmd
    					tmp=tmp.siguiente
    					oper=tmp.cmd
    					tmp=tmp.siguiente
    					cond2=tmp.cmd
    					showFileCondition(cond1,oper,cond2,nameFile)	
    				else:
    					print("directo aquii")
    					showFile(nameFile)

    			
    		elif(SimbActual == "PR_insert"):
    			print("hello broo")
    			cantidad=0;
    			tmp=tmp.siguiente
    			SimbActual=tmp.token
    			if(SimbActual=="PR_table"):
    				tmp=tmp.siguiente
    				nameFile=tmp.cmd +".csv"#capturando nombre de la 
    				tmp=tmp.siguiente
    				SimbActual=tmp.token
    				while (SimbActual!="tkn_parentesis_cerrado"):
    					tmp=tmp.siguiente
    					SimbActual=tmp.token
    					#print("en el primer while "+SimbActual)
    					while (SimbActual!="tkn_coma" and SimbActual!="tkn_parentesis_cerrado"):
    						t=tmp.cmd
    						tmp=tmp.siguiente
    						SimbActual=tmp.token
    					listCampos.append(t) 
    				if(checkfile(nameFile)==True):
    					t=[]
	    				file = open(nameFile,"r")
	    				reader=csv.reader(file)
	    				for row in reader:
	    					t.append(row)
	    				file.close()

	    				ofile =open(nameFile,"w")
	    				write = csv.writer(ofile,delimiter=",")
	    				for row in t:
	    					print(row)
	    					write.writerow(row)

	    				write.writerow(listCampos)
	    				ofile.close()
    				else:
		    			print("No existe la tabla "+ nameFile)  				
                if(SimbActual=="PR_register"):
                	tmp=tmp.siguiente
                	nameFile=tmp.cmd +".csv"#capturando nombre de la 
                	tmp=tmp.siguiente #(
                	tmp=tmp.siguiente  # date 
                	cantidad=tmp.cmd
                	print("cantidad "+str(cantidad))
                	tmp=tmp.siguiente #)
                	tmp=tmp.siguiente 
                	SimbActual=tmp.token
                	if(checkfile(nameFile)==True):
                		print("trabajando")
                		funRegister(nameFile,cantidad)
                	else:
                		print("No existe la tabla "+ nameFile)

    		elif(SimbActual == "PR_update"):
    			print("actualizar datos ")
    		elif(SimbActual == "PR_delete"):
    			print("delete")
    			tmp=tmp.siguiente
    			nameFile=tmp.cmd+".csv"
    			tmp=tmp.siguiente
    			tmp=tmp.siguiente
    			c1=tmp.cmd
    			tmp=tmp.siguiente
    			tmp=tmp.siguiente
    			c2=tmp.cmd
    			SimbActual=tmp.token
    			deleteRegister(c1,c2,nameFile)

    			#showFile(nameFile)
    			#print("print"+ nameFile)

    			"""tmp=tmp.siguiente
    			nameFile=tmp.cmd+".csv"
    			tmp=tmp.siguiente #where
    			print("..-->"+SimbActual)"""


    	#**********************
    		else:
    			tmp=tmp.siguiente
    			SimbActual=tmp.token
    			print("--> "+ SimbActual)
    	


    		

    	"""while(pilaSG.Top()!='$'):
                #print("SA->"+SimbActual)
            pilaSG.Print()
            if(esTerminal(pilaSG.Top()) or pilaSG.Top()=='$'):
        		if(pilaSG.Top()==SimbActual):
        			pilaSG.Pop()
        			tmp=tmp.siguiente
        			SimbActual=tmp.token 
        		else:
        			print('     >>> nose esperaba esto  '+ tmp.cmd +"     linea"+ str(tmp.line))
                            
            else:
        			#print("existe "+pilaSG.Top()+"  "+ SimbActual+"  :"+str(existeProduccion(pilaSG.Top(),SimbActual)))
        		if(existeProduccion(pilaSG.Top(),SimbActual)):
        			nt=pilaSG.Top()
        			t=SimbActual
        			tmpe=[]
        			pilaSG.Pop();
        			for x in range(0,len(TablaSintactica)):
        				if nt==TablaSintactica[x][0] and t==TablaSintactica[x][1]:
        					tmpe=TablaSintactica[x][2]
        	   		tmpe.reverse()
        	   				#print(tmpe)
        	   		for i in tmpe:
        	   			if i!='vacio':
        	   				pilaSG.Push(i)
        	   					
        	   				#print("existe"+str(existeProduccion(pilaSG.Top(),SimbActual)))
        		else:

                            #tmp=tmp.siguiente
            				print("   >>>error no existe produccion "+pilaSG.Top()+" CON "+ tmp.cmd +"    linea  "+str(tmp.line))
            				break
        			
          	 	
    	print(" ")
        pilaSG.Print()
        """
    		
	#print(pilaSG.Top())


#***************LECTURA DE ARCHIVO .csv
def lectura_archivo_CSV(fileName):
	"""results = []
	with open(fileName) as File:
	    reader = csv.DictReader(File)
	    for row in reader:
	        results.append(row)
	    print results"""
	with open(fileName) as File:
	    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
	    for row in reader:
	        print(row)



#************MENU PRINCIPAL****************		     

if __name__ == '__main__':
	#cmdinput = input('>>>: ')
	listatokens=Lista();
	#print data_reglon;
	procesamiento(listatokens)
    #hallando_tablaSimbolos(listatokens)
	AnalizadorSintactico(listatokens)







