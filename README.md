![AutoAttackScript](https://github.com/VloDIE/MinecraftAutoAttackScript/blob/main/assets/images/dark_theme/logo.png)

### 📕Select launguage to read: [English](#English-guide) or [Russian](#Russian-guide)
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## English guide
- ## Guide Content:  
1. 💡 [Idea](#💡Idea)
2. 📂 [Installation](#📂Installation)
3. 💿 [Opportunity List](#💿Opportunity-List)
4. 🕹 [Usage](🕹#Use)

## **💡 Idea**  
> Inspired by - https://github.com/vin350/AutoAttack  
>
The idea was to make a script that runs on top of the game, and allows you to just hold down the lmb and hit the sword's cooldown recovery timings without-oops 
(_so far, the lmb operation has not been implemented due to obscure bugs_)  

## **📂Installation**  
- #### For users
> This use case does not require Python installed on your computer.

Download the Zip archive of the repository, unzip it to a convenient location. Run the **AutoAttackGui.exe** file, enjoy
- #### For developers  
> This already requires Python installed, version 3.10 or higher, and added to the PATH environment variable.
> 
Install and unzip the Zip archive of the repository. In the open script directory, click on the folder path, write **cmd** there, and paste the command there:
```
pip install -U -r requirements.txt
```
Wait for the necessary modules to be installed, and then create._  

## **💿Opportunity List** ##
1. The button "**On**" is strangely enough responsible for enabling and disabling the script by changing the Caps lock status.  
> (also immediately when you enter the program, no matter what status caps lock has, it is changed to inactive for convenience).  
2. In this version, the radio buttons are responsible for selecting the key, when pressing which the script will click. (In the future I intend to move this to the settings menu)
3. The theme change button in the top right corner when clicked simply changes the theme.
4. And the last item for now, the ["**Support**"](https://www.donationalerts.com/r/vlodie) button, which works exactly the same way as in this text.  

## **🕹Using**.  
After running **AutoAttackGui.exe** you will see the program's interface:   
<p align="center">
<img src="https://github.com/VloDIE/MinecraftAutoAttackScript/assets/137058732/56ed9e74-da1c-4aaa-8d5b-53e8c2a7fce0" alt="[gui-example" width="300"/>  
</p>

- Click **ON** , then you will have a special sound played, depending on the status of the script. And the status of Caps will change, thus activating the script. Now when you press the selected key below.  
> (Currently only **B** and **XButton1** or the 5th mouse key)

- The script will emulate the sword's cd timing without missing a click.
You can also adjust the script's activity by simply pressing **Caps Lock**, and the script will also play sounds.

---

# Russian guide
- ## Контент руководства:  
1. 💡  [Идея](#💡Идея)
2. 📂 [Установка](#📂Установка)
3. 💿 [Список возможностей](#💿Список-возможностей)
4. 🕹 [Использование](#🕹Использование)

## **💡Идея**  
> Вдохновлялся - https://github.com/vin350/AutoAttack  
>
Идея была сделать скрипт, работающий поверх игры, и позволяющий просто зажать лкм и без-ошибочно попадать в тайминг восстановления кд меча 
(_пока-что работа с лкм не реализованна из-за непонятных ошибок_)  

## **📂Установка**  
- #### Для пользователей
> При этом варианте использования установленный на компьютер Python не требуется.

Скачайте Zip архив репозитория, распакуйте его в удобное для вас место. Запустите файл **AutoAttackGui.exe**, наслаждайтесь
- #### Для разработчиков  
>  Здесь уже требуется установленный Python, версии не ниже 3.10, и добавленный в переменную среды PATH.
Установите и распакуйте Zip-архив репозитория. В открытой директории скрипта нажмите на путь папки, напишите туда **cmd**, и вставьте туда команду:
```
pip install -U -r requirements.txt
```
_Дождитесь установки необходимых модулей, и творите._  

## **💿Список возможностей** ##
1. Кнопка "**On**" как ни странно отвечает за включение и отключение скрипта, путём изменения статуса Caps lock.  
> (также сразу при заходе в программу в независимости от того, какой статус у caps lock'а, он сменяется на неактивный для удобства)  
2. В данной версии радио-кнопки кнопки отвечают за выбор клавиши, при зажатии которой скрипт и будет кликать. (В будущем я намерен перенести это в меню настроек)
3. Кнопка смены темы в правом верхнем углу при нажатии просто меняет тему оформления.
4. И последний на данный момент элемент, кнопка ["**Поддержать**"](https://www.donationalerts.com/r/vlodie), которая работает точно также, как и в этом тексте.  

## **🕹Использование**  
После запуска **AutoAttackGui.exe** вы увидите интерфейс программы:   
<p align="center">
<img src="https://github.com/VloDIE/MinecraftAutoAttackScript/assets/137058732/56ed9e74-da1c-4aaa-8d5b-53e8c2a7fce0" alt="[gui-example" width="300"/>  
</p>

- Нажмите кнопку **ON** , после чего у вас проиграется специальный звук, в зависимости от статуса скрипта. И сменится статус Caps'а, тем самым активируется скрипт. Теперь при зажатии выбранной клавиши ниже  
> (На данный момент только **B** и **XButton1** или-же 5-я клавиша мыши)

- скрипт будет не промахиваясь по таймингу кд у меча эмулировать нажатии лкм.
Также можно регулировать активность скрипта просто нажимая **Caps Lock**, и при этом как также будут воспроизводится звуки.
