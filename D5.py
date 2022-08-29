'''
(env) $ pip install django-allauth


'''

# D5.3
# В модуле D4 создавалась страница редактирования новости с помощью дженерика UpdateView.
# По аналогии создать страницу редактирования своего профиля и
# реализовав для него проверку наличия аутентификации с помощью миксина - какого .
# В файле настроек проекта добавьте адрес, по которому Django будет перенаправлять пользователей после успешного входа в систему.

# D5.4
# Используя только пакет allauth, реализуйте в своем приложении News Portal возможность входа в систему,
# а также регистрации по почте или через Google-аккаунт.
# В файле настроек добавьте адрес на страницу входа,
# по которому перенаправится неавторизованный пользователь при попытке перейти на защищенные страницы.

# Для редактирования профиля автора/пользователя - переход на /account/profile/
#from django.contrib.auth.decorators import login_required
#@login_required
#def view_foo(request):
#    if request.method == 'GET':
#        form = CreatePost()
#        return render(request, 'testapp/create.html', {'form': form})
#    elif request.method == 'POST':
#        form = CreatePost(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.current_user = UserProfile.objects.get(user=request.user)
#            post.save()
#            return redirect('index')
#