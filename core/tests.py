import datetime

from django.test import TestCase,Client
from django.contrib.auth.models import User

from core.models import *
from core.forms import *
     
class TestCenario5(TestCase):
    def setUp(self):
        self.client = Client()
        self.criar_url = "/new/caderno/"

    def testeSucess(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeSucess1(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "", descricao = "fsdfhsfhs")
        except :
            return True
        return False

    def testeSucess2(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhssdvbsdvsdsdvsdsdvvsfddddddddddddddddddddddddddddddddddddd"})
            query = Caderno.objects.get(nome = "", descricao = "fsdfhsfhssdvbsdvsdsdvsdsfffffffffffffffffffffffffffffffffffffffffffffdvvsd")
        except :
            return True
        return False
        
    def testeSucess3(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "123" , "descricao" : ""})
            query = Caderno.objects.get(nome = "123", descricao = "")
        except : 
            return True
        return False

    def testeSucess4(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "12345678901234561" , "descricao" : "fdfdfdfd"})
            query = Caderno.objects.get(nome = "12345678901234561", descricao = "fdfdfdfd")
        except : 
            return True
        return False

    def testeSucess5(self):
        try :
            response = self.client.post(self.criar_url,{"nome" : "12345678901234561" , "descricao" : "123456789012345678901234567890"})
            query = Caderno.objects.get(nome = "123", descricao = "123456789012345678901234567890")
        except : 
            return True
        return False

class TestCenario6(TestCase):
    def setUp(self):
        self.caderno = Caderno.objects.create(nome = "cena6", descricao = "teste123")
        self.client = Client()
        self.editar_url = "editar/caderno/" + str(self.caderno.pk)

    def testeSucess(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeSucess1(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "", descricao = "fsdfhsfhs")
        except :
            return False
        return False

    def testeSucess2(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "1234567890123456" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "1234567890123456", descricao = "fsdfhsfhs")
        except :
            return False
        return False

    def testeSucess3(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "1234567890123456111111" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "123456789012345611111", descricao = "fsdfhsfhs")
        except :
            return False
        return False

    def testeSucess4(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "12345678" , "descricao" : ""})
            query = Caderno.objects.get(nome = "12345678", descricao = "")
        except :
            return False
        return False

    def testeSucess5(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "12345678" , "descricao" : "fsdfhsfhssdvbsdvsdsdvsdsdvvsfddddddddddddddddddddddddddddddddddddd"})
            query = Caderno.objects.get(nome = "12345678", descricao = "")
        except :
            return False
        return False

    def testeSucess6(self):
        try :
            response = self.client.post(self.editar_url,{"nome" : "12345678" , "descricao" : "123456789012345678901234567890"})
            query = Caderno.objects.get(nome = "12345678", descricao = "")
        except :
            return False
        return False


class TestCenario7(TestCase):
    def setUp(self):
        self.caderno = Caderno.objects.create(nome = "cena7", descricao = "teste123")
        self.client = Client()
        self.excluir_url = "excluir/caderno/" + str(self.caderno.pk)

    def testeSucess(self):
        try :
            response = self.client.post(self.excluir_url,{"nome" : "cena7" , "descricao" : "teste123"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeSucess1(self):
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

    def testeSucess(self):
        try :
            response = self.client.post(self.consultar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"teste123")

    def testeSucess1(self):
        try :
            response = self.client.post(self.consultar_url,{"nome" : "teste123" , "descricao" : "fsdfhsfhs"})
            query = Caderno.objects.get(nome = "teste123", descricao = "fsdfhsfhs")
        except :
            return False
        self.assertEquals(query.nome,"naopresente")
