from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, True)
        # 추가 저장 필드: nickname, profile_path
        
        user.nickname = data.get('nickname')
        user.profile_path = data.get('profile_path')

        user.save()
        return user