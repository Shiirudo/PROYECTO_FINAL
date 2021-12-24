from django import forms 
from .models import Post, Category

#//Rigida: choices = [('Objetivo 1: Fin de la Pobreza','Objetivo 1: Fin de la Pobreza'), ('Objetivo 2: Hambre Cero','Objetivo 2: Hambre Cero'), ('Objetivo 3: Salud y Bienestar','Objetivo 3: Salud y Bienestar'), ('Objetivo 4: Educación de Calidad','Objetivo 4: Educación de Calidad'), ('Objetivo 5: Igualdad de Género','Objetivo 5: Igualdad de Género'), ('Objetivo 6: Agua Limpia y Saneamiento','Objetivo 6: Agua Limpia y Saneamiento'), ('Objetivo 7: Energía Asequible y No Contaminante','Objetivo 7: Energía Asequible y No Contaminante'), ('Objetivo 8: Trabajo Decente y Crecimiento Económico','Objetivo 8: Trabajo Decente y Crecimiento Económico'), ('Objetivo 9: Industria, Innovación e Infraestructura','Objetivo 9: Industria, Innovación e Infraestructura'), ('Objetivo 10: Reducción de las Desigualdades','Objetivo 10: Reducción de las Desigualdades'), ('Objetivo 11: Ciudades y Comunidades Sostenibles','Objetivo 11: Ciudades y Comunidades Sostenibles'), ('Objetivo 12: Producción y Consumo Responsables','Objetivo 12: Producción y Consumo Responsables'), ('Objetivo 13: Acción por el Clima','Objetivo 13: Acción por el Clima'), ('Objetivo 14: Vida Submarina','Objetivo 14: Vida Submarina'), ('Objetivo 15: Vida de Ecosistemas Terrestres','Objetivo 15: Vida de Ecosistemas Terrestres'), ('Objetivo 16: Paz, Justicia e Instituciones Sólidas','Objetivo 16: Paz, Justicia e Instituciones Sólidas'), ('17: Alianzas para Lograr los Objetivos','17: Alianzas para Lograr los Objetivos'), ('Otras...', 'Otras...'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Añadir un títutlo a tu Post💬'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Añadir un title_tag🧠'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '....✍️👻'}),
        
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Añadir un títutlo a tu Post💬'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Añadir un title_tag🧠'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '....✍️👻'}),
        
        }