from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from bancos.models import ContaBancaria
from .models import Entrada, Saida
from .forms import EntradaModelForm, SaidaModelForm


##### CRUD DE ENTRADAS ######
class EntradaListView(ListView):
    '''LISTAGEM DE ENTRADAS'''
    model = Entrada
    template_name = 'entrada/entrada_list.html'
    context_object_name = 'entradas'

# Detalhes de uma Entrada
class EntradaDetailView(DetailView):
    '''DETALHAMENTO DE ENTRADAS'''
    model = Entrada
    template_name = 'entrada/entrada_detail.html'
    context_object_name = 'entrada'

class EntradaCreateView(CreateView):
    '''CRIAÇÃO DE ENTRADA'''
    model = Entrada
    template_name = 'entrada/entrada_form.html'
    form_class = EntradaModelForm
    success_url = reverse_lazy('entrada-list')


class EntradaUpdateView(UpdateView):
    '''ATUALIZAÇÃO DE UMA ENTRADA'''
    model = Entrada
    template_name = 'entrada/entrada_form.html'
    form_class = EntradaModelForm
    success_url = reverse_lazy('entrada-list')


class EntradaDeleteView(DeleteView):
    '''EXCLUSÃO DE UMA ENTRADA'''
    model = Entrada
    template_name = 'entrada/entrada_confirm_delete.html'
    success_url = reverse_lazy('entrada-list')


##### CRUD DE SAÍDAS ######
class SaidaListView(ListView):
    '''LISTAGEM DE SAÍDAS'''
    model = Saida
    template_name = 'saida/saida_list.html'
    context_object_name = 'saidas'


class SaidaDetailView(DetailView):
    '''DETALHES DE UMA SAÍDA'''
    model = Saida
    template_name = 'saida/saida_detail.html'
    context_object_name = 'saida'

class SaidaCreateView(CreateView):
    '''CRIAÇÃO DE UMA SAÍDA'''
    model = Saida
    template_name = 'saida/saida_form.html'
    form_class = SaidaModelForm
    success_url = reverse_lazy('saida-list')


class SaidaUpdateView(UpdateView):
    '''ATUALIZAÇÃO DE UMA SAÍDA'''
    model = Saida
    template_name = 'saida/saida_form.html'
    form_class = SaidaModelForm
    success_url = reverse_lazy('saida-list')


class SaidaDeleteView(DeleteView):
    '''EXCLUSÃO DE UMA SAÍDA'''
    model = Saida
    template_name = 'saida/saida_confirm_delete.html'
    success_url = reverse_lazy('saida-list')


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Pega o mês do GET, se não houver, usa o mês atual
        mes = self.request.GET.get('mes', timezone.now().month)
        ano = timezone.now().year  # você pode querer adicionar uma opção para o ano

        entradas = Entrada.objects.filter(data__month=mes, data__year=ano)
        saidas = Saida.objects.filter(data__month=mes, data__year=ano)
        contas = ContaBancaria.objects.all()

        context['entradas'] = entradas
        context['saidas'] = saidas
        context['mes_atual'] = mes  # Adiciona o mês atual ao contexto
        context['bancos'] = contas

        # Define a lista de meses
        context['meses'] = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        return context
