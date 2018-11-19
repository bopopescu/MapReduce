from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import tarefa, tarefapalavras, pilhaprocessos

def cadastrarPOST(request):
    job = tarefa()
    job.titulo = request.POST.get('titulo')
    job.conteudo = request.POST.get('conteudo')
    job.save()
    verficar = request.POST.get('keys')
    for palavra in verficar.split(','):
        pala = tarefapalavras()
        pala.id_tarefa = job
        pala.palavra = palavra
        pala.save()
    pilhaProcesso = pilhaprocessos()
    pilhaProcesso.id_tarefa = job
    pilhaProcesso.status_processo = 0
    pilhaProcesso.save()
    return render(request, "tarefa/cadastrar.html", {'mensagem': "Cadastro feito sucesso. Verifique o status: ", 'tipo': "success"})

def cadastrarGET(request):
    return render(request, "tarefa/cadastrar.html", {'mensagem': "", 'tipo': ""})

def cadastrarRequest(request):
    if request.method == "POST":
        return cadastrarPOST(request)
    else:
        return cadastrarGET(request)
#############################################################
def gerarStringPalavras(palavras):
    pala = ""
    for pal in palavras:
        if pala != "":
            pala += ", "+pal.palavra
        else:
            pala += pal.palavra
    return pala

@csrf_exempt
def carregarTarefaModal(request):
    idTarefa = request.POST.get('id')
    ta = tarefa.objects.get(id=idTarefa)
    palavras = gerarStringPalavras(tarefapalavras.objects.filter(id_tarefa=idTarefa))
    taPilha = pilhaprocessos.objects.get(id_tarefa=idTarefa)
    mensagem = render_to_string('ajax/listarTarefa.html', {'tarefa': ta, 'pilha':taPilha, 'palavras': palavras})
    return JsonResponse({'html' :mensagem, 'titulo': ta.titulo})

def visualizarTarefaGET(request):
    tarefas = tarefa.objects.all()
    return render(request, 'tarefa/listarTarefa.html', {'tarefa': tarefas})

def visualizarTarefaPOST(request):
    return None

def visualizarTarefa(request):
    if request.method == "POST":
        return visualizarTarefaPOST(request)
    else:
        return visualizarTarefaGET(request)
#############################################################
def listarComputadores(request):
    tarefas = tarefa.objects.all()
    return render(request, 'computador/listarComputador.html', {'tarefa': tarefas})

def carregarTarefa(idTarefa):
    tf = tarefa.objects.filter(idTarefa).get
    palavras = list()
    pala = tarefapalavras.objects.get(id_tarefa=idTarefa)
    for pa in pala:
        palavras.append({'id':pa.id, "palavra":pa.palavra})
    return {'idTarega': tf.id, 'contudo': tf.conteudo, 'palavras': palavras}

@csrf_exempt
def verificarTarefas(request):
    abertos = pilhaprocessos.objects.filter(status_processo=0)
    if abertos:
        trabalhos = list()
        for job in abertos:
            trabalhos.append(carregarTarefa(job))
        return {'tarefas': True, 'trabalhos': trabalhos}
    else:
        return {'tarefas': False}

