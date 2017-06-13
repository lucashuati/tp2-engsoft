import datetime

from django.test import TestCase,Client
from django.contrib.auth.models import User

from core.models import *
from core.forms import *


class TestCenario1(TestCase):
    def setUp(self):
        self.client = Client()
        self.criar_url = "/new/listaCaderno/"

    def testeCriaNorma(self):
        try :
        response = self.client.post(self.criar_url,{"nome" : "testeSim" , "descricao" : "lala", "cadernos" : "[1,2]"} )
        query = ListaCaderno.objects.get(nome = "testesim", descricao = "lala", cadernos = ["1", "2"])
        except :
            return False
        self.assertEquals(query.nome, "testeSim")

    def TesteNomeNull_DescriNull_CaderNull(self):
        try :
            response = self.client.post(self.criar_url, {"nome" : "" , "descricao" : "" , "cadernos" : "[]"})
            query = ListaCaderno.objects.get(nome = "", descricao= "" ,cadernos=[""])
        except:
            return True
        return False

    def TesteNomeNull_DescriOK_CaderNull(self):
        try :
            response = self.client.post(self.criar_url, {"nome" : "" , "descricao" : "kk" , "cadernos" : "[]"})
            query = ListaCaderno.objects.get(nome = "", descricao= "kk" ,cadernos=[""])
        except:
            return True
        return False


    def TesteNomeNull_DescriOK_CaderOK(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "", "descricao": "okok", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="", descricao="okok", cadernos=["1", "2"])
        except:
            return True
        return False


    def TesteNomeOK_DescriNull_CaderNull(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "Testeok", "descricao": "", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="Testeok", descricao="", cadernos=[""])
        except:
            return True
        return False


    def TesteNomeOK_DescriOK_CaderNull(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "Testeokok", "descricao": "kk", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="Testeokok", descricao="kk", cadernos=[""])
        except:
            return True
        return False


    def TesteNomeOK_DescriNull_CaderOK(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "TesteOkok", "descricao": "", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="TesteOkok", descricao="", cadernos=["1", "2"])
        except:
            return True
        return False


    def TesteNomeNull_DescriNull_CaderOK(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "", "descricao": "", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="", descricao="", cadernos=["1", "2"])
        except:
            return True
        return False
    def TesteNomeExcede_descriOk_CadernoOk(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "teste", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="teste", cadernos=["1", "2"])
        except:
            return True
        return False

    def TesteNomeExcede_descriNULL_CadernoOk(self):
        try:
            response = self.client.post(self.criar_url,
                                        {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="", cadernos=["1", "2"])
        except:
            return True
        return False

    def TesteNomeExcede_descriOk_CadernoNULL(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "teste", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="teste", cadernos=[])
        except:
            return True
        return False

    def TesteNomeExcede_descriExcede_CadernoOk(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "tttttttttttttttttttttttttttttttttttttttt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="tttttttttttttttttttttttttttttttttttttttt", cadernos=["1", "2"])
        except:
            return True
        return False

    def TesteNomeExcede_descriExcede_CadernoNul(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "tttttttttttttttttttttttttttttttttttttttt", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="tttttttttttttttttttttttttttttttttttttttt", cadernos=[])
        except:
            return True
        return False

    def TesteNomeOk_descriExcede_CadernoOk(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "kk", "descricao": "tttttttttttttttttttttttttttttttttttttttt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kk", descricao="tttttttttttttttttttttttttttttttttttttttt", cadernos=["1", "2"])
        except:
            return True
        return False

    def TesteNomeOk_descriOk_CadernoNUll(self):
        try:
            response = self.client.post(self.criar_url, {"nome": "kkk", "descricao": "tttttttttttttttttttttttttttttttttttttttt", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkk", descricao="", cadernos=[])
        except:
            return True
        return False


    def TesteNomeNull_descriExcede_CadernoOk(self):
        try:
            response = self.client.post(self.criar_url,{"nome": "", "descricao": "tttttttttttttttttttttttttttttttttttttttt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="", descricao="tttttttttttttttttttttttttttttttttttttttt",cadernos=["1", "2"])
        except:
            return True
        return False


    def TesteNomeNULL_descriOk_CadernoNUll(self):
        try:
            response = self.client.post(self.criar_url,{"nome": "", "descricao": "tttttttttttttttttttttttttttttttttttttttt","cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="", descricao="tttttttttttttttttttttttttttttttttttttttt", cadernos=[])
        except:
            return True
        return False


class TestCenario2(TestCase):
    def setUp(self):
        self.lista = ListaCaderno.objects.create(nome = "cena2", descricao = "teste123")
        self.client = Client()
        self.edit_url = "editar/listaCaderno/" + str(self.lista.pk)

    def TestecriaNormal(self):
        try :
            response = self.client.post(self.edit_url,{"nome" : "testeSim" , "descricao" : "lala", "cadernos" : "[1,2]"} )
            query = ListaCaderno.objects.get(nome = "testesim", descricao = "lala", cadernos = ["1", "2"])
        except :
            return False
        self.assertEquals(query.nome, "testeSim")
    def TesteNomeNull_DescriNull_CaderNull(self):
        try :
            response = self.client.post(self.edit_url, {"nome" : "" , "descricao" : "" , "cadernos" : "[]"})
            query = ListaCaderno.objects.get(nome = "", descricao= "" ,cadernos=[""])
        except:
            return True
        return False

    def TesteNomeNull_DescriOK_CaderNull(self):
        try :
            response = self.client.post(self.edit_url, {"nome" : "" , "descricao" : "kk" , "cadernos" : "[]"})
            query = ListaCaderno.objects.get(nome = "", descricao= "kk" ,cadernos=[""])
        except:
            return True
        return False


    def TesteNomeNull_DescriOK_CaderOK(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "", "descricao": "okok", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="", descricao="okok", cadernos=["1", "2"])
        except:
            return True
        return False


    def TesteNomeOK_DescriNull_CaderNull(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "Testeok", "descricao": "", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="Testeok", descricao="", cadernos=[""])
        except:
            return True
        return False


    def TesteNomeOK_DescriOK_CaderNull(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "Testeokok", "descricao": "kk", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="Testeokok", descricao="kk", cadernos=[""])
        except:
            return True
        return False


    def TesteNomeOK_DescriNull_CaderOK(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "TesteOkok", "descricao": "", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="TesteOkok", descricao="", cadernos=["1", "2"])
        except:
            return True
        return False


    def TesteNomeNull_DescriNull_CaderOK(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "", "descricao": "", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="", descricao="", cadernos=["1", "2"])
        except:
            return True
        return False
    def TesteNomeExcede_descriOk_CadernoOk(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "tt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="tt", cadernos=["1", "2"])
        except:
            return True
        return False

    def TesteNomeExcede_descriNUll_CadernoOk(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="", cadernos=["1", "2"])
        except:
            return True
        return False
    def TesteNomeExcede_descriOk_CadernoNULL(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "tt", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="tt", cadernos=[])
        except:
            return True
        return False
    def TesteNomeExcede_descriNull_CadernoNull(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="", cadernos=[])
        except:
            return True
        return False
    def TesteNomeExcede_descriExcede_CadernoOk(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "ttttttttttttttttttttttttttttttttttttttttttttt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="ttttttttttttttttttttttttttttttttttttttttttttt", cadernos=["1", "2"])
        except:
            return True
        return False
    def TesteNomeExcede_descriExcede_CadernoNull(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "descricao": "ttttttttttttttttttttttttttttttttttttttttttttt", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkkkkkkkkkkkkkkkkkkkkkkkkkkk", descricao="ttttttttttttttttttttttttttttttttttttttttttttt", cadernos=[])
        except:
            return True
        return False
    def TesteNomeOk_descriExcede_CadernoOk(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kk", "descricao": "ttttttttttttttttttttttttttttttttttttttttttttt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="kk", descricao="ttttttttttttttttttttttttttttttttttttttttttttt", cadernos=["1", "2"])
        except:
            return True
        return False
    def TesteNomeOK_descriExcede_CadernoNull(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "kkk", "descricao": "ttttttttttttttttttttttttttttttttttttttttttttt", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="kkk", descricao="ttttttttttttttttttttttttttttttttttttttttttttt", cadernos=[])
        except:
            return True
        return False
    def TesteNomeNull_descriExcede_CadernoOk(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "", "descricao": "ttttttttttttttttttttttttttttttttttttttttttttt", "cadernos": "[1,2]"})
            query = ListaCaderno.objects.get(nome="", descricao="ttttttttttttttttttttttttttttttttttttttttttttt", cadernos=["1", "2"])
        except:
            return True
        return False
    def TesteNomeNull_descriExcesso_CadernoNUll(self):
        try:
            response = self.client.post(self.edit_url, {"nome": "", "descricao": "ttttttttttttttttttttttttttttttttttttttttttttt", "cadernos": "[]"})
            query = ListaCaderno.objects.get(nome="", descricao="ttttttttttttttttttttttttttttttttttttttttttttt", cadernos=[])
        except:
            return True
        return False


class TesteCenario3(TestCase):
    def setUp(self):
        self.lista = Caderno.objects.create(nome = "cena7", descricao = "teste123", , cadernos=["1", "2"])
        self.client = Client()
        self.excluir_url = "excluir/listaCaderno/" + str(self.caderno.pk)

    def testeCria_ok(self):
        try :
            response = self.client.post(self.excluir_url,{"nome" : "cena7" , "descricao" : "teste123", "cadernos" : "[1,2]"})
            query = ListaCaderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs", , cadernos=["1", "2"])
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeExclui(self):
        try :
            response = self.client.post(self.excluir_url,{"nome" : "cena7" , "descricao" : "teste123", "cadernos" : "[1,2]"})
            query = ListaCaderno.objects.get(nome = "cena7", descricao = "teste123", cadernos=["1", "2"])
        except :
            return False
        return False

class TestCenario4(TestCase):
    def setUp(self):
        self.client = Client()
        self.consultar_url = "/listaCadernos/"

    def testeBusca(self):
        try :
            response = self.client.post(self.consultar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs", "cadernos" : "[1,2]"})
            query = ListaCaderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs", cadernos=["1", "2"])
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeBusca_Fail(self):
        try :
            response = self.client.post(self.consultar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs", "cadernos" : "[1,2]"})
            query = ListaCaderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs", cadernos=["1", "2"])
        except :
            return False
        self.assertEquals(query.nome,"naopresente")




class TestCenario5(TestCase):
    def setUp(self):
        self.client = Client()
        self.criar_url = "/new/caderno/"

    def testeCriaNormal(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")


    def testeNomeNulo_DescriNull(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "" , "descricao" : ""})
            query = Caderno.objects.get(nome = "", descricao = "")
        except :
            return True
        return False

    def testeNomeNulo_DescriNorml(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "" , "descricao" : "fdfdfdfd"})
            query = Caderno.objects.get(nome = "", descricao = "fdfdfdfd")
        except :
            return True
        return False

    def testeNomeNulo_DescriExcede(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "" , "descricao" : "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd"})
            query = Caderno.objects.get(nome = "", descricao = "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd")
        except :
            return True
        return False

    def testeNomeNorml_DescriNULL(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "teste123" , "descricao" : ""})
            query = Caderno.objects.get(nome = "teste123", descricao = "")
        except :
            return True
        return False

    def testeNomeNorml_DescriNorml(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "teste123" , "descricao" : "123456"})
            query = Caderno.objects.get(nome = "teste123", descricao = "123456")
        except :
            return True
        return False

    def testeNomeNorml_DescriExcede(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd")
        except :
            return True
        return False


    def testeNomeExcede_DescriNull(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "12345678901234561" , "descricao" : ""})
            query = Caderno.objects.get(nome = "12345678901234561", descricao = "")
        except : 
            return True
        return False

    def testeNomeExcede_DescriNorml(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "12345678901234561" , "descricao" : "123456"})
            query = Caderno.objects.get(nome = "12345678901234561", descricao = "123456")
        except : 
            return True
        return False

    def testeNomeExcede_DescriExcede(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "12345678901234561789797979" , "descricao" : "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd"})
            query = Caderno.objects.get(nome = "12345678901234561789797979", descricao = "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd")
        except : 
            return True
        return False


class TestCenario6(TestCase):
    def setUp(self):
        self.caderno = Caderno.objects.create(nome = "cena6", descricao = "teste123")
        self.client = Client()
        self.editar_url = "editar/caderno/" + str(self.caderno.pk)

    def testeCriaNormal(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeNomeNulo_DescriNull(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "" , "descricao" : ""})
            query = Caderno.objects.get(nome = "", descricao = "")
        except :
            return False
        return False

    def testeNomeNulo_DescriNorml(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "" , "descricao" : "123456"})
            query = Caderno.objects.get(nome = "", descricao = "123456")
        except :
            return False
        return False

    def testeNomeNulo_DescriExcede(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "" , "descricao" : "12345678901234567890123456789999999"})
            query = Caderno.objects.get(nome = "", descricao = "12345678901234567890123456789999999")
        except :
            return False
        return False

    def testeNomeNorml_DescriNull(seUlllf):
        try :
            response = self.client.post(self.editar_url,{"nome" : "123456" , "descricao" : ""})
            query = Caderno.objects.get(nome = "123456", descricao = "")
        except :
            return False
        return False

    def testeNomeNorml_DescriNorml(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "123456" , "descricao" : "123456"})
            query = Caderno.objects.get(nome = "123456", descricao = "123456")
        except :
            return False
        return False

    def testeNomeNorml_DescriExcede(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "123456" , "descricao" : "12345678901234567890123456789999999"})
            query = Caderno.objects.get(nome = "123456", descricao = "12345678901234567890123456789999999")
        except :
            return False
        return False

    def testeNomeExcede_DescriNull(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "12345678907897897979797979" , "descricao" : ""})
            query = Caderno.objects.get(nome = "12345678907897897979797979", descricao = "")
        except :
            return False
        return False

    def testeNomeExcede_DescriNorml(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "12345678907897897979797979" , "descricao" : "123456"})
            query = Caderno.objects.get(nome = "12345678907897897979797979", descricao = "123456")
        except :
            return False
        return False

    def testeNomeExcede_DescriExcede(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "12345678907897897979797979" , "descricao" : "12345678901234567890123456789999999"})
            query = Caderno.objects.get(nome = "12345678907897897979797979", descricao = "12345678901234567890123456789999999")
        except :
            return False
        return False

    


class TestCenario7(TestCase):
    def setUp(self):
        self.caderno = Caderno.objects.create(nome = "cena7", descricao = "teste123")
        self.client = Client()
        self.excluir_url = "excluir/caderno/" + str(self.caderno.pk)

    def testeCria_ok(self):
        try :
            response = self.client.post(self.excluir_url,{"nome" : "cena7" , "descricao" : "teste123"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeExclui(self):
        try :
            response = self.client.post(self.excluir_url,{"nome" : "cena7" , "descricao" : "teste123"})
            query = Caderno.objects.get(nome = "cena7", descricao = "teste123")
        except :
            return False
        return False

class TestCenario8(TestCase):
    def setUp(self):
        self.client = Client()
        self.consultar_url = "/cadernos/"

    def testeBusca(self):
        try :
            response = self.client.post(self.consultar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeBusca_Fail(self):
        try :
            response = self.client.post(self.consultar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"naopresente")
