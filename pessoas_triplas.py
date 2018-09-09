table_pessoa = open('base_com_nomes.csv', 'r')
turtle_pessoa = open('turtle_base_com_nome.ttl', 'w')

prefix = ('@base <http://dbpedia.org/resource/Category:> .\n@prefix dbc: <http://dbpedia.org/resource/Category:> . \n' +
'@prefix ra: <ra:http://www.w3.org/2012/7/ra3.owl#> . \n@prefix dc: <http://purl.org/dc/elements/1.1/> . \n' +
'@prefix foaf: <http://xmlns.com/foaf/0.1/> .')

turtle_pessoa.write(prefix + '\n\n')

count = 1

for line in table_pessoa:
    line = line.strip().replace('; ', ';').split(";")
    id_pessoa = '<' + line[0].replace(' ','_') + '> a foaf:person ;'
    idade = '\tfoaf:age \"' + str(line[2]) + '\" ;'
    tipo_aph = '\tra:sofre ra:' + line[6] + str(count) + ' .'
    class_aph = 'ra:'+ line[6] + str(count) + ' a ra:tipo_aph ' ' ;'
    cidade = '\tdbc:List_municipalities_in_Brazil dbc:' + line[3].replace(' ','_')+' ;'
    causa = '\tra:causa ra:' + line[4].replace(' ','_') + ' ;'
    date = '\tdc:date \"' + line[1] +'/' + line[5] + '\" .'
    turtle_pessoa.write(id_pessoa + '\n' + idade + '\n' + tipo_aph + '\n' + class_aph + '\n' + cidade + '\n' + causa + '\n' + date + '\n\n')
    count =  count+1

    
   
  

#print(id_cidade + '\n' + nome + '\n' + date + '\n' + causa + '\n' + tipo + '\n' + total_ocorrencias + '\n\n')


"""pessoa 1 a foaf:person;
   foaf age "idade";
    ra:sofre ra:trauma.
ra:trauma a ra:Tipo_aph;
    dbr: city_brazyl "cidade" ;
    ra: causa " "
    dc: date "06/18" """