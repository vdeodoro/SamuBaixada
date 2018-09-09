table_cidade = open('base_cidade.csv', 'r')
turtle_cidade = open('turtle_cidade.ttl', 'w')

prefix = ('@base <http://dbpedia.org/resource/Category:> .\n@prefix dbc: <http://dbpedia.org/resource/Category:> . \n' +
    '@prefix ra: <ra:http://www.w3.org/2012/7/ra3.owl#> . \n@prefix dc: <http://purl.org/dc/elements/1.1/> . \n' +
'@prefix foaf: <http://xmlns.com/foaf/0.1/> .')

turtle_cidade.write(prefix + '\n\n')

count = 1

for line in table_cidade:
    line = line.strip().replace('; ', ';').split(";")
    id_cidade = '<' + line[1].replace(' ','_')+ '_' + line[0] + '_' + line[3] + '> a dbc:List_municipalities_in_Brazil ;'
    ocorre = '\tra:ocorre' + ' ra:acidente' + '_' + str(count) + ' ;'
    municipio = '\tfoaf:name \"'+ line[1]+'\" .'
    acidente = 'ra:acidente' + '_' + str(count) + ' a ra:causa ;'
    tipo_acidente = '\tra:tipo ra:' + line[2].replace(' ','_') + '_' + str(count) + ' .'
    trauma = 'ra:'+ line[2].replace(' ','_') + '_' +  str(count) + ' a ra:' + line[4] + ' ;'
    nome_ocorrencia = '\tfoaf:name \"'+ line[2] + '\" ;'
    date = '\tdc:date \"' + line[0] +'/' + line[3] + '\" ;'
    total_ocorrencias = '\tra:ocorrencias \"' + line[5] + '\" .'
    count = count+1
    #print(id_cidade + '\n' + ocorre + '\n' + municipio + '\n' + acidente + '\n' + tipo_acidente + '\n' + trauma + '\n' + nome_ocorrencia + '\n' + date + '\n' + total_ocorrencias + '\n\n')
    turtle_cidade.write(id_cidade + '\n' + ocorre + '\n' + municipio + '\n' + acidente + '\n' + tipo_acidente + '\n' + trauma + '\n' + nome_ocorrencia + '\n' + date + '\n' + total_ocorrencias + '\n\n')


#class_acidente = '\tra:' + line[4].replace(' ','_') + '_' + line[0] + '_' + line[3] + ' a ra:tipo_aph ' ' ;'
    #turtle_cidade.write(id_cidade + '\n' + nome + '\n' + date + '\n' + causa + '\n' + tipo + '\n' + total_ocorrencias + '\n\n')

#print(id_cidade + '\n' + nome + '\n' + date + '\n' + causa + '\n' + tipo + '\n' + total_ocorrencias + '\n\n')

"""<Belford_Roxo_06_16> a dbc:List_municipalities_in_Brazil ;
    ra:Ocorre ra:acidente_06_2016 ;
    dbc:List_municipalities_in_Brazil dbc:belford_roxo;
ra:acidente_06_2016 a ra:causa ;
    ra:tipo ra:auto x auto ;
ra:auto x auto a ra:trauma ;
    foaf:name "auto_auto" ;
    dc:date "06/2016" ;
    ra:ocorrencias "3" ."""