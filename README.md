Change wallpapers on Linux from different cities in the world. 


http://api.deckchair.com/v1/cameras
Он возвращает здоровенный массив. Для навигации пользуемся поиском по странице. Нас интересует значение поля {_id} Чтобы получить последнее фото с камеры заходим по этому адресу:
http://api.deckchair.com/v1/viewer/camera/:id
Вместо :id вписываем ID камеры, которые мы узнали из предыдущего пункта. Например, для Парижа ссылка будет выглядеть вот так:
http://api.deckchair.com/v1/viewer/camera/5568862a7b28535025280c72


https://github.com/Deckchair/DeckchairDocumentation