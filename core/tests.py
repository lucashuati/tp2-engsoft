import datetime

from django.test import TestCase,Client
from django.contrib.auth.models import User

from core.models import *
from core.forms import *
     
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
