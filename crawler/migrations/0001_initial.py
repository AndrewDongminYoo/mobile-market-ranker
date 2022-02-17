# Generated by Django 3.2.12 on 2022-02-15 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=64, verbose_name='앱 이름')),
                ('icon_url', models.URLField(verbose_name='아이콘 이미지')),
                ('package_name', models.CharField(max_length=64, verbose_name='앱 아이디')),
            ],
            options={
                'verbose_name': '애플리케이션',
                'verbose_name_plural': '애플리케이션',
            },
        ),
        migrations.CreateModel(
            name='TrackingApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('deal_type', models.CharField(max_length=16, verbose_name='기간')),
                ('market', models.CharField(max_length=16, verbose_name='마켓명')),
                ('rank_type', models.CharField(max_length=16, verbose_name='순위 타입')),
                ('app_name', models.CharField(max_length=64, verbose_name='앱 이름')),
                ('icon_url', models.URLField(verbose_name='아이콘 이미지')),
                ('package_name', models.CharField(max_length=64, verbose_name='앱 아이디')),
                ('rank', models.IntegerField(default=200, verbose_name='순위')),
                ('date_hour', models.CharField(max_length=16, verbose_name='일시')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.app', verbose_name='애플리케이션')),
            ],
            options={
                'verbose_name': '추적 결과',
                'verbose_name_plural': '추적 결과',
            },
        ),
        migrations.CreateModel(
            name='Ranked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('date', models.CharField(default='2022021509', max_length=16, verbose_name='날짜')),
                ('deal_type', models.CharField(choices=[('realtime_rank', '실시간'), ('market_rank', '일간')], max_length=16, verbose_name='기간')),
                ('market', models.CharField(choices=[('google', '구글 플레이'), ('apple', '앱 스토어'), ('one', '원 스토어')], max_length=16, verbose_name='마켓명')),
                ('rank_type', models.CharField(choices=[('free', '무료 순위'), ('paid', '유료 순위'), ('gross', '매출 순위')], max_length=16, verbose_name='순위 타입')),
                ('app_type', models.CharField(choices=[('game', '게임'), ('app', '애플리케이션')], max_length=16, verbose_name='앱 타입')),
                ('market_appid', models.CharField(max_length=64, verbose_name='스토어 아이디')),
                ('rank', models.IntegerField(verbose_name='순위')),
                ('app_name', models.CharField(max_length=64, verbose_name='앱 이름')),
                ('icon_url', models.URLField(verbose_name='아이콘 이미지')),
                ('package_name', models.CharField(max_length=64, verbose_name='앱 아이디')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.app', verbose_name='애플리케이션')),
            ],
            options={
                'verbose_name': '랭킹',
                'verbose_name_plural': '랭킹',
            },
        ),
        migrations.CreateModel(
            name='OneStoreDL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('market_appid', models.CharField(max_length=32, verbose_name='원스토어 ID')),
                ('genre', models.CharField(max_length=128, verbose_name='장르')),
                ('downloads', models.IntegerField(null=True, verbose_name='다운로드수')),
                ('volume', models.CharField(max_length=128, verbose_name='용량')),
                ('released', models.DateField(null=True, verbose_name='출시일')),
                ('icon_url', models.URLField(default=None, verbose_name='앱 아이콘')),
                ('app_name', models.CharField(default=None, max_length=128, verbose_name='앱 이름')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.app', verbose_name='애플리케이션')),
            ],
            options={
                'verbose_name': '원스토어 순위',
                'verbose_name_plural': '원스토어 순위',
            },
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('app_name', models.CharField(max_length=64, verbose_name='앱 이름')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.app', verbose_name='애플리케이션')),
            ],
            options={
                'verbose_name': '순위 추적',
                'verbose_name_plural': '순위 추적',
            },
        ),
    ]