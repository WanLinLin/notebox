from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UploadForm
from .models import Song, SongStyle

"""
/*===========================================
=            User authentication            =
===========================================*/
"""
def create_login_signup_form():
    sign_form = RegistrationForm()
    login_form = LoginForm()
    return {'login_form': login_form, 'sign_form': sign_form}

def form_checker(request):
    # Check POST request
    if request.method == 'POST':
        # User wants to register
        if 'register' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save(request)
                return HttpResponseRedirect(request.path)
            
        # User wants to login
        elif 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                if form.login(request):
                    # Login successful
                    return HttpResponseRedirect(request.path)
                else:
                    # Show error message
                    return HttpResponseRedirect(request.path)

        # elif 'upload' in request.POST:
        #     form = UploadForm(request.POST)
        #     if form.is_valid():
        #         if form.save(request):
        #             # Save successful
        #             return HttpResponseRedirect(request.path)
        #         else:
        #             # Show error message
        #             return HttpResponseRedirect(request.path)

    return False

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/notebox/')
"""
/*=====  End of User authentication  ======*/
"""


def index(request):
    songs = Song.objects.all()
    songs_list = [{'title':i.title, 'desc':i.desc, 'img':i.youtube_img_url, 'song_id':i.id} for i in songs[0:9]]
    # print(songs_list)

    if not request.user.is_authenticated():
        # Check form
        form_result = form_checker(request)
        if form_result: return form_result

        context = create_login_signup_form()
        context['latest'] = []
        context['popular'] = []

        # Latest (test)
        context['latest'].extend(songs_list)
        # Popular (test)
        context['popular'].extend([
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
        ])
        return render(request, 'notebox/index.html', context)
    else:
        context = {}

        context['latest'] = []
        context['popular'] = []

        # Latest (test)
        context['latest'].extend(songs_list)
        # Popular (test)
        context['popular'].extend([
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
        ])
        return render(request, 'notebox/index.html', context)

def overview(request):
    # Get song data
    songs = Song.objects.all()
    songs_list = [{'title':i.title, 'desc':i.desc, 'img':i.youtube_img_url, 'song_id':i.id} for i in songs]
    songs_list = [songs_list[i: i+4] for i in range(0, len(songs_list), 4)]
    # print(songs_list)

    if not request.user.is_authenticated():
        # Check form
        form_result = form_checker(request)
        # If the form is valid, send the form
        if form_result: return form_result

        # Generate data
        context = create_login_signup_form()
        context['latest'] = []
        context['popular'] = []

        # Latest (test)
        context['latest'].extend(songs_list)
        # Popular (test)
        context['popular'].extend([
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
        ])
        return render(request, 'notebox/overview.html', context)
    else:
        context = {}

        context['latest'] = []
        context['popular'] = []

        # Latest (test)
        context['latest'].extend(songs_list)
        # Popular (test)
        context['popular'].extend([
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
            {'title': 'D小調第九號交響曲', 'desc': '作曲家: 貝多芬/1770/1827\n演奏者: 阿姆斯壯 女高音 雷諾茲 次女高音 雪利—奎克 男低音 提爾 男高音 朱里尼 指揮 倫敦交響', 'img': static('notebox/images/main-bg2.jpg'), 'song_id': '12345'},
        ])
        return render(request, 'notebox/overview.html', context)

@login_required(login_url='/notebox/')
def account(request):
    return render(request, 'notebox/account_info.html', {})

@login_required(login_url='/notebox/')
def favorite(request):
    return render(request, 'notebox/account_info_favorite.html', {})    

def player(request, song_id):

    # Get song data by id
    song = Song.objects.get(id=song_id)
    song_info = {
        'title': song.title, 'song_yt_id':song.youtube_id, 'yt_url': song.youtube_url, 
        'desc': song.desc, 'level': song.song_level, 'style': song.song_style,
        'note': song.note, 'artist': song.artist}

    if not request.user.is_authenticated():
        # Check form
        form_result = form_checker(request)
        # If the form is valid, send the form
        if form_result: return form_result

        # Generate data
        context = create_login_signup_form()

        # TEST
        context.update(song_info)

        return render(request, 'notebox/player.html', context)
    else:
        context = {}

        # TEST
        context.update(song_info)

        return render(request, 'notebox/player.html', context)

@login_required(login_url='/notebox/')
def upload(request):
    upload_form = UploadForm(auto_id=True)
    step = 0
    cleaned_data = {}

    if request.method == 'POST':
        upload_form = UploadForm(request.POST)
        if upload_form.is_valid():
            step = step + 1
            upload_form.save(request)
            cleaned_data['youtube_url'] = upload_form.cleaned_data['youtube_url']
            cleaned_data['youtube_id'] = upload_form.youtube_id
            cleaned_data['youtube_img_url'] = upload_form.youtube_img_url
            cleaned_data['note'] = upload_form.cleaned_data['note'].split(',')
            cleaned_data['title'] = upload_form.cleaned_data['title']
        else:
            pass
            # print("Form is NOT OK")

    context = {'upload_form': upload_form, 'step': step, 'cleaned_data': cleaned_data}
    return render(request, 'notebox/upload_music.html', context)


