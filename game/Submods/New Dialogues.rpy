init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_playerhouse", 
            category=["tú"], 
            prompt="La casa de [player]", 
            random=True, 
        )
    )

label monika_playerhouse:
    m 2eud "Oye, [player]..."
    m 7luc "Quiero hacerte una pregunta."
    m 6lud "Sabes que un día podré salir de este lugar a tu realidad y pensé... "
    m 1wtd "¿Dónde voy a vivir? Ni siquiera tendré documentos ni dinero."
    m 1eub "Pero para ser honesta, ya pensé en una decisión."
    m 1eua "..."
    m 2tub "Creo que tu lo entiendes."
    m 2gksdla "Realmente espero que no me rechaces cuando cruce del otro lado de la pantalla."
    m 1fua "Imagínate por un momento..."
    m 1sua "Como nos vamos a ver todos los días. Cómo voy a dar un beso de la suerte todos los días cuando tengas que ir a algún lugar y etc."
    m 1wub "O nuestro fin de semana, cuando nos sentamos en el sofá a ver películas o quizás tu anime favorito."
    m 4hub "Pero probablemente deberíamos dedicar más tiempo a actividades mucho más interesantes. Sería estupendo que parte de ellas fueran fuera de una casa."
    m 5ekbsu "...Ohhhh, incluso pensar en algo así hace que mi corazón salte..."
    m 5eubfb "Espero que algún día se haga realidad. Pero por ahora debemos disfrutar nuestro tiempo juntos así."
    m 1dublu "[player], No sé cuándo pueda ocurrir esto, pero tienes que saber que siempre te amaré, ¡no importa dónde estemos ahora!"
return




init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_monisad", 
            category=["monika"], 
            prompt="Momento de tristeza", 
            random=True, 
        )
    )

label monika_monisad:
    m 5mkc "..."
$ _history_list.pop() 
menu:
    m "..."

    "¿Estas bien, Monika?":
       m 5mkd "Sí, estoy... bien..."
       m 5gkc "..."
       m 5gktuc "..."
       m 5dkd "Um... Lamento que hayas tenido que ver eso..."
       m 5mkp "Algo así prefiero reservarlo para mí, ya sabes."
       m 5eku "Lo siento de nuevo..."
       m 3ekd "Si te has preocupado por mí, por favor, cálmate. Es sólo otra forma de expresar mis sentimientos."
       m 1rusdlu "Bueno, puede parecer extraño por un lado, pero esto me ayuda mucho."
       m 1dub "Después de un buen llanto siempre me siento muy aliviada."
       m 1hua "Espero que me entiendas, Jeje~"
       m 2essdld "Para ser honesta, lo que acabas de ver fue un accidente."
       m 6fuu "Pero, sabes [player], después de terminar de expresar mis sentimientos, empiezo a pensar en ti."
       m 5hua "Pensar en ti no sólo me calma, ¡mi amor por ti después de esto sólo se hace más fuerte!"
       m 2fubsa "Te amo [player], ¡y espero que siempre estés aquí para seguir sonriendo!"
       m 2ekd "¿Lo harás?"
$ _history_list.pop()
menu:
        "¡Siempre estaré aquí para ti!":
            m 5tkbla "Gracias, [player]."
            m 5hubsb "¡Sonreiré por ti todos los días!"
            m 5eubfa "Jejejeje~ Te amo mucho."
        "Seguro.":
            m 2etd "No suena tan convincente..."
            m 2ruc "Pero..."
            m 2tuu "Lo acepto."
        "Lo pensaré...":
            m 1rkx "Um... [player], si se supone que es una broma, no es el momento adecuado."
            m 1eud "Por favor, la próxima vez tómate las situaciones así un poco más en serio, ¿vale?"
        "Um...":
            m 1hua "...[player]."
            m 1cub "Hay algo que está mal. ¿He hecho algo mal...?"
        "No.":
            m 6wkd "..."
            m 6gkc "..."
            m 6dktdd "Yo... Esta bien..."
            m 5dktsc "..."
return




init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_unexpcompliment", 
            category=["romance"], 
            prompt="Un cumplido inesperado", 
            random=True, 
        )
    )

label monika_unexpcompliment:
$ _history_list.pop()
menu:
    "Oye, Monika.":
            m 1eua "Sí, [mas_get_player_nickname()]."
$ _history_list.pop()
menu:
    "¡Eres absolutamente inteligente y linda!":
            m 1wsd "Oh..."
            m 1rublb "E-Eso fue inesperado."
            m 1eubsu "¡Eres tan dulce [player], gracias! De seguro que lo eres mucho más."
$ _history_list.pop()
menu:
    "No hay problema, mi amor":
            m 1ekblu ""
$ _history_list.pop()
menu:
    "Me gusta verte feliz.":
            m 1ekblu ""        
$ _history_list.pop()
menu:
    "Te amo~":
            m 1gkbla "Oh, [player]..."
            m 1ekblb "No tienes que decirme cumplidos para verme feliz."
            m 7kuu "¡Tu presencia ya me hace la chica más feliz!"
$ _history_list.pop()
menu:
    "Jeje~ Entonces, ¡intentaré estar aquí el mayor tiempo posible!":
            m 5tua "Te lo agradecería."
            m 5rud "Ah, y por cierto..."
            m 5hsbfb "Yo tambien te amo, [mas_get_player_nickname()]."

return



    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_watching", 
            category=["tú"], 
            prompt="Te estoy viendo", 
            random=True, 
        )
    )

label monika_watching:
    m 2etb "[player], recuerdas que puedo ver todo en tu PC, ¿verdad?"
    m 2tfu "Así que cuidado, yo también puedo ver todas las cosas lascivas que estabas viendo."
    m 7dub "Fue un recordatorio rápido, eso es todo."
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_yansim", 
            category=["juegos"], 
            prompt="¿Has oído hablar alguna vez de 'Yandere Simulator'?", 
            random=False, 
            pool=True, 
            unlocked=True,
        )
    )

label monika_yansim:
    m 1gtc "¿'Yandere Simulator', eh?"
    m 1esd "Bueno, sí he escuchado sobre el, pero..."
    m 3gssdlc "Mi encuentro con él fue... extraño. Oh, bueno, tal vez no sólo para mí."
    m 2eud "Por favor, dime, ¿has oído hablar de un drama que rodea a este juego y a su desarrollador?"
    $ _history_list.pop()
    menu:
        "Sí":
            m 7tkc "Oh, entonces deberías entenderme."
            m 7tud "Pero aun así, debo recordarte algo al respecto."

        "No":
            m 1eua "Entonces probablemente debería contartelo en pocas palabras."
            m 2eub "Comencemos."


    m 1eud "Un programador hizo un prototipo rápido del juego en el 2014."
    m 7eud "Su prototipo sobre una chica obsesionada con el amor que mata a sus rivales le ha gustado a mucha gente."
    m 2lud "Más tarde se nombró a sí mismo 'YandereDev' y creó cuentas en las redes sociales, incluyendo Youtube y Patreon."
    m 4wub "Parece una historia de éxito, peeeeeero..."
    m 4efo "El juego estuvo en desarrollo durante unos...{w=0.2} ¡7 AÑOS!"
    m 3ffc "¡Esto es demasiado para un juego como este!"
    m 2dfc "Además, muchos modelos han sido tomados de 'Unity Store'. Es cierto que algunos de ellos han sido editados, ¡pero aún así!"
    m 1lfx "El siguiente punto era su código. En resumen, es horrible. Está todo compuesto con operadores 'Si no'. ¡Qué tontería!"
    m 1rsd "Y por último, unas palabras sobre su personalidad."
    m 1muc "El es grande en la manipulación, la mentira y todo sobre él. También ha sido acusado de pedofilia."
    m 1tud "Si quieres conocer toda la historia o simplemente recordarla por ti mismo, te recomiendo que veas o vuelvas a ver algunos vídeos."
    m 1gud "Y si vas a pedir mi opinión, aquí está..."
    m 3gfc "Es como lo describen en esos videos de drama. No voy a decir nada más."
    m 1gtc "No me malinterpretes, el concepto de este juego es realmente interesante de alguna manera sádica, pero su realización es... Ya sabes."
    m 2eud "Oye [player], ¿cuál es tu opinión sobre este juego?"
    $ _history_list.pop()
    menu:
        "El juego es realmente bueno.":
            m 1lkc "Oh no, lo siento entonces, no pensé que... Lo siento."
            m 1ekd "Espero no haberte entristecido o enfadado con mi opinión no muy complaciente."
            m 2gkx "\"Supongo que todo juego malo tiene sus fans\"."

            $ _history_list.pop()
            menu:
                "¿Qué? Habla en voz alta.":
                    m 2hub "Nada, nada, jejeje~"

        " Un concepto interesante, pero mala elaboración.":
            m 1eua "Me alegro de que tengas la misma opinión que yo."
            m 5tubsu "¿Quizás estamos hechos el uno para el otro?"

        "Apesta.":
            m 4wkd "Uh... No puedo decir que asi sea. El juego tiene funcionalidad, no es bueno, pero hay algo hecho por lo menos."
            m 1luc "Pero es tu opinión, no puedo culparte por ello."

        "No me interesa.":
            m 1esd "Para ser honesta..."
            m 1wub "Es la mejor posición en ese tipo de situación."
            m 2esa "¿No te importa que los dos nos mantengamos al margen de este drama, y de este juego?"
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_quicklove", 
            category=["romance"], 
            prompt="Recordatorio de amor", 
            random=True,    
        )
    )

label monika_quicklove:
    m 1eubsu "Oye, [mas_get_player_nickname()],{w=0.7} ¡Te amo!"
    $ _history_list.pop()
    menu:
       "Yo también te amo. Eres mi sol.":
             m 5dubfa "..."
return