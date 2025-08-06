import pygame
import textwrap

class ModoHistoria2D:
    def __init__(self, pantalla, manejador):
        self.pantalla = pantalla
        self.manejador = manejador
        self.fuente = pygame.font.SysFont('arial', 28)
        
        # Cargar todas las imágenes de fondo
        self.fondos = {
            'colegio': pygame.image.load('assets/images/Fondo colegio.png').convert(),
            'campo': pygame.image.load('assets/images/Fondo campo.png').convert(),
            'tapera': pygame.image.load('assets/images/Fondo tapera.png').convert()
        }
        
        # Cargar todos los personajes
        self.personajes = {
            'antonio': pygame.image.load('assets/images/antonio.png.png').convert_alpha(),
            'luis': pygame.image.load('assets/images/luiz.png').convert_alpha(),
            'john_baker': pygame.image.load('assets/images/john_baker.png').convert_alpha(),
            'padre': pygame.image.load('assets/images/padre de antonio.png').convert_alpha(),
            'madre': pygame.image.load('assets/images/madre de antonio.png').convert_alpha(),
            'farias': pygame.image.load('assets/images/viejo farias.png').convert_alpha(),
            'comisario': pygame.image.load('assets/images/Comisario.png').convert_alpha(),
            'hombre_cicatriz': pygame.image.load('assets/images/hombre de la cicatriz.png').convert_alpha()
        }
        
        # Escalar personajes al mismo tamaño que Antonio
        tamaño_antonio = self.personajes['antonio'].get_size()
        for nombre, imagen in self.personajes.items():
            if nombre != 'antonio':
                # Hacer los personajes 5 veces más pequeños
                nuevo_tamaño = (tamaño_antonio[0] // 5, tamaño_antonio[1] // 5)
                self.personajes[nombre] = pygame.transform.scale(imagen, nuevo_tamaño)
        
        # También escalar Antonio para que sea consistente
        nuevo_tamaño_antonio = (tamaño_antonio[0] // 5, tamaño_antonio[1] // 5)
        self.personajes['antonio'] = pygame.transform.scale(self.personajes['antonio'], nuevo_tamaño_antonio)
        
        # Definir las escenas del juego basadas en la novela
        self.escenas = [
            {
                'nombre': 'Capítulo 1: De vuelta a clase',
                'fondo': 'colegio',
                'personajes': [],
                'posiciones': {},
                'textos': [
                    "Era el 10 de marzo y las clases habían comenzado otra vez. Sin embargo, el verano continuaba, empujando con días cálidos y secos la llegada del otoño austral.",
                    "Eran días para continuar corriendo por la playa, zambulléndose en el mar, y no para estar sentado en el salón de clase de aquel colegio de Montevideo.",
                    "Antonio miró por la ventana y suspiró. Era un largo año el que quedaba por delante. ¡Y el verano se había pasado tan rápido!",
                    "Dio un vistazo alrededor y saludó a un par de amigos con una morisqueta. Esa mañana se había dormido y había llegado a clase cuando ya estaban todos sentados.",
                    "Miró hacia la derecha: en el banco de al lado había un muchacho que no conocía y que, al sentir la mirada, lo miró a su vez y le sonrió.",
                    "Tenía un rostro curtido por el sol y una sonrisa franca. No parecía un chico de ciudad, tenía ese aire de los que se han criado en el campo.",
                    "Parece buen tipo – pensó Antonio."
                ]
            },
            {
                'nombre': 'Capítulo 2: El nuevo amigo',
                'fondo': 'colegio',
                'personajes': [],
                'posiciones': {},
                'textos': [
                    "Salieron en tropel, cada uno buscando a sus amigos. Porque lo importante del primer día de clase era precisamente eso: el reencuentro.",
                    "En el patio, se fueron armando numerosas ruedas, donde todos hablaban a la vez, queriendo ser cada uno el primero en contar todo lo que había hecho en las vacaciones de verano.",
                    "Se acercó su compañero del banco de la derecha, aquél que él no conocía y que le había parecido un buen tipo, con su aire de venir de campo.",
                    "Yo soy Luis Martínez – dijo, dirigiéndose a Antonio, pero abarcando en el gesto a los demás – y es el primer día que vengo aquí.",
                    "Yo soy Antonio Ferreira – le dijo cuando Luis le dio la mano, agregando de inmediato: ¿Dónde estudiaste antes?",
                    "En el interior, en Durazno. Mis padres viven en el campo y yo estudiaba en el Liceo de Durazno, porque allí vivía mi abuela y yo me quedaba con ella.",
                    "Pero este verano se murió, así que me mandaron a Montevideo, a casa de una tía.",
                    "¿Y dónde viven tus padres?",
                    "Tienen un campo cerca de Cañada Seca.",
                    "¿Cañada qué?",
                    "Cañada Seca – repitió Luis. Es un pueblito a unos doscientos y pico de quilómetros de aquí, más cerca de trescientos.",
                    "¿Y vos sos jinete?",
                    "Bastante. Pero mi padre es mucho más. Él doma los caballos que usamos."
                ]
            },
            {
                'nombre': 'Capítulo 3: Otoño en Montevideo',
                'fondo': 'colegio',
                'personajes': [],
                'posiciones': {},
                'textos': [
                    "Durante la segunda hora de clase, Antonio pensó con desagrado en la actitud de sus amigos, haciéndose los vivos y pretendiendo burlarse y tomar el pelo al nuevo compañero.",
                    "Sólo porque venía de otro lado y tenía al parecer costumbres más formales. Pero ser diferente en algo no lo hacía ni mejor ni peor, solamente era algo distinto.",
                    "Resolvió hablarle a los amigos para que aflojaran la mano. No era que a Luis Martínez le hiciera falta que lo defendieran.",
                    "De este modo, los días siguientes Luis se fue integrando al grupo, con Antonio como decidido factótum de su montevideanización.",
                    "Así marchó con ellos un sábado al Parque Rodó, un domingo al Estadio y otras veces al cine.",
                    "Antonio se preocupaba de irle explicando lo que hacían y veían, para facilitarle el entrar en caja.",
                    "Cuando, al mes, una compañera de clase los invitó a la fiesta de sus quince años, marcharon todos a una discoteca en Carrasco.",
                    "Al poco rato, Luis andaba en el medio de la pista, zangoloteándose como el mejor al ritmo de Pink Floyd.",
                    "Antonio, que se sacudía cerca de él, le palmeó la espalda, diciéndole: ¡Bien, Luis, muy bien! Parece que te sacaste las espuelas.",
                    "Y Luis, con una gran sonrisa de oreja a oreja, mostrándole la linda gurisa que sostenía de la mano, respondió: Obligado cualquiera pelea."
                ]
            },
            {
                'nombre': 'Capítulo 4: Vacaciones de invierno',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Llegó Semana Santa y todos tomaron rumbos distintos. Luis se fue a pasarla al campo, otros se fueron a distintos puntos de la costa o del interior, y Antonio se quedó en Montevideo.",
                    "Cuando a fines junio fueron a Montevideo los padres de Luis, los de Antonio los invitaron a comer y congeniaron rápidamente. Eran gente linda.",
                    "Al final de la cena, el padre de Luis le dijo a Antonio: Nosotros queremos agradecerte todo lo que has hecho para ayudar a Luis, como él nos ha contado.",
                    "Como tú has conseguido urbanizar a este paisano, nosotros queremos retribuírtelo haciéndote campero. Así que te venís a pasar las vacaciones de julio a Cañada Seca, ¿estamos?",
                    "Antonio saltó de contento y tartamudeó unas gracias. Se volvió a sentar y preguntó: ¿Qué tengo que llevar?",
                    "Yo diría que mucho unto sin sal – dijo el padre con una carcajada.",
                    "No te preocupes – dijo la madre de Luis – que yo le digo a tu madre lo que vas a necesitar.",
                    "Ya en el viaje de ida, inofensivamente y sin que los dos se dieran cuenta, los papeles se fueron invirtiendo.",
                    "Ahora era Antonio el que preguntaba y Luis el que explicaba y enseñaba.",
                    "¿Y aquella allá en lo alto?",
                    "Es una vieja tapera. La llaman La tapera del Inglés.",
                    "¿Hay ingleses por acá?",
                    "No. Hubo uno en el siglo pasado.",
                    "Cuando se bajaron en Cañada Seca, la familia en pleno los estaba esperando: el padre, la madre y la hermanita de Luis, que tenía nueve años.",
                    "El pueblo era brevísimo. Una calle larga, de ocho o diez cuadras, cruzada por otras tantas transversales.",
                    "¿Por qué se llama Cañada Seca?",
                    "¿Ves allí – le dijo el padre –, que hay como un cañadón, como una zanja grande? En el siglo pasado eso era una cañada, pero en unas crecientes muy grandes el agua cortó otro cauce un quilómetro más allá y éste quedó seco. Por eso el nombre."
                ]
            },
            {
                'nombre': 'Capítulo 5: Noche de luces malas',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis', 'farias'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400), 'farias': (400, 300)},
                'textos': [
                    "Salieron después de almorzar rumbo a la laguna grande que había mencionado el viejo Farías.",
                    "Aunque a los muchachos les habría divertido más ir ellos solos, no pudieron negarse a que el viejo les hiciera de guía en aquel hervidero de tarariras, como él decía.",
                    "Luis atravesó en el recado, sentándose sobre ellas, dos tacuaras finas de un par de metros, que iban a utilizar de mojarreros.",
                    "El viejo Farías llevaba una bolsita con sus aparejos y ató un roncador a los tientos.",
                    "Cuando llegaron a la laguna, se bajaron de los caballos en el pesquero favorito del viejo: un breve remanso, con algo de arena en la orilla y protegido por un corpulento tarumán.",
                    "Los muchachos, apurados, ataron los caballos, armaron los mojarreros y se pusieron a pescar de inmediato, con las lombrices que habían traído de la quinta.",
                    "El viejo, pachorriento, empezó a organizar el campamento. Sacó su maleta del recado y de allí extrajo primero un farol, que colgó de una rama baja del tarumán.",
                    "Después juntó leña, armó y prendió un fuego y, finalmente, sacó de su inagotable maleta una botella de caña, le dio un largo beso, la puso en el suelo, apoyándola en el tronco, y dijo con satisfacción: Ahora sí.",
                    "Recién después que terminaron de comer, el viejo se decidió a pescar. Eligió tres buenos dientudos del montón de mojarras que habían sacado los muchachos y encarnó los grandes anzuelos de otros tantos aparejos.",
                    "Los arrojó a distintos lados de la laguna, a pozos que él conocía, según dijo, clavó el roncador y atravesó sobre él las líneas de los aparejos.",
                    "Había tormenta hacia el Sur, y los relámpagos empezaban a iluminar aquella parte del cielo. Dos horas después, la tormenta y los relámpagos estaban más cerca.",
                    "Vamos a levantar campamento – dijo el viejo –. Tenemos una hora de viaje y la tormenta se arrima.",
                    "Empezaron a subir la ladera hacia la tapera del inglés y, cuando estaban a unas dos cuadras, dijo Antonio: Hay algo que brilla en la tapera.",
                    "El viejo Farías miró y exclamó: ¡Ave María Purísima! ¡Boitatá!",
                    "¿Qué es eso? – preguntó Antonio, pero el viejo no contestó.",
                    "Cuando estaban más cerca, Antonio vio que era como una brillante bola de fuego, algo menor que una pelota de fútbol, que parecía posada en un arbusto.",
                    "Parece un efecto láser – dijo Antonio, y espoleó su caballo para acercarse.",
                    "¡Muchacho, vení p'acá! ¡No te arrimes a eso! – le gritó el viejo Farías, y era tal la urgencia y la desesperación de su voz, que Antonio sofrenó y dio vuelta.",
                    "¿Qué pasa? ¿Por qué no puedo ir a ver? ¿Usted tiene miedo a eso?",
                    "¡Claro que le tengo! ¿Vos sabés lo que es eso?",
                    "No.",
                    "¡Una luz mala!",
                    "Pues alumbra bastante. ¿Qué es una luz mala?",
                    "Un ánima en pena.",
                    "Antonio miró a Luis y, a la luz de un relámpago, lo vio serio y con expresión de miedo. Y a él se dirigió: ¿Qué te pasa a vos? ¿Qué es un ánima en pena?",
                    "Es un alma en pena, que no puede llegar al cielo – dijo Luis.",
                    "Antonio entró a dudar. Bueno, ¿y qué hay que hacer?",
                    "Irse – dijo el viejo, y dobló hacia el costado para hacer un largo rodeo en torno a la tapera.",
                    "Los muchachos lo siguieron, Antonio dándose vuelta para mirar la bola fosforescente que seguía posada en el arbolito.",
                    "Después de andar dos o tres cuadras, el viejo volvió a doblar rodeando la tapera, y la luz mala dejó de verse cuando la taparon los altos muros de piedra.",
                    "Cuando ya estaban por sobrepasar las ruinas, Antonio, que seguía mirando, dijo: ¡Miren, hay otra bola luminosa de este lado!",
                    "El viejo Farías giró la cabeza, miró y entró en pánico: ¡Es la misma y nos está siguiendo! –y, clavando espuelas, arrancó el galope y se perdió en las sombras, los muchachos atrás y las tarariras chicoteándole el caballo."
                ]
            },
            {
                'nombre': 'Capítulo 6: Cuentos de fogón',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis', 'farias'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400), 'farias': (400, 300)},
                'textos': [
                    "Como todos dormían cuando llegaron, recién al desayuno pudieron contar sus aventuras de la noche anterior: la pesca, la luz mala y la huida, deteniéndose especialmente en la luz mala.",
                    "¡Pobrecita! – dijo la madre de Luis –. Debían por lo menos haberle rezado un Padrenuestro.",
                    "Yo no sé – dijo Antonio.",
                    "No estaba la cosa para acordarse – agregó Luis.",
                    "El padre se reía, sobre todo del susto del viejo Farías.",
                    "Cuando lo cuente en alguna rueda de mate lo va a haber adornado tanto que ni ustedes reconocerían el sucedido. Pero hubiera pagado para verle la cara al viejo.",
                    "Al otro día, a media mañana, marcharon los cinco. Tomaron un camino secundario hasta llegar a un solitario almacén, perdido en medio del campo.",
                    "Tenían de un lado un galpón y del otro una cantidad de bretes y mangueras, porque allí se hacían remates ganaderos una vez al mes.",
                    "En el potrero llano que estaba detrás del boliche, se veían claramente marcadas tres rectas sendas.",
                    "Tres sendas cual tres galones, hacen capitán al campo – recitó el padre de Luis.",
                    "El lugar ya estaba lleno de gente, aunque las pencas eran por la tarde. Algunos autos, varias camionetas y muchos caballos moteaban el campo en torno al boliche.",
                    "Él y Luis se separaron del resto de la familia y empezaron a recorrerlo todo.",
                    "Entraron al boliche, donde el mostrador estaba atestado de parroquianos; pasaron al galpón donde otro contingente numeroso participaba del remate de las apuestas.",
                    "Siguieron a los asadores, donde tres hombres arrimaban brasas a una respetable cantidad de carne; miraron todo lo que se ofrecía en los distintos puestos de venta.",
                    "Y pasaron por una mesa improvisada donde en dos latones se vendía asado con cuero.",
                    "Cuando terminaron la recorrida se reencontraron con la familia de Luis.",
                    "Y, ¿qué te parece esto? – le preguntó el padre.",
                    "Es fantástico – dijo Antonio –, aquí hay gente de dos siglos.",
                    "Quisiera saber en cuál me ubicas a mí – dijo el padre y se rió.",
                    "¿Vieron los parejeros?",
                    "No los habían visto y el padre los acompañó a ver los seis caballos que, de a dos, protagonizarían las tres pencas de la tarde.",
                    "Les fue mostrando lo que, a su juicio, eran defectos y virtudes de cada uno, en la cabeza, el lomo, el encuentro, el anca, los aplomos.",
                    "Y concluyó que el que más le gustaba era el tostado.",
                    "¿Le vas a jugar a ése? – preguntó Antonio.",
                    "No, m'hijo, yo porfío pero no apuesto.",
                    "Fueron a almorzar a una larga mesa de tablas y caballetes. La madre traía platos y cubiertos envueltos en un paño, que colocó en la mesa.",
                    "Hubo que vencer una fuerte resistencia de Antonio a enfrentar un pedazo de asado con cuero, con aquella pelambre de un lado, pero al final aceptó probarlo.",
                    "Cuando probó el primer pedazo, puso una cara de enorme placer.",
                    "¿Qué te parece?",
                    "Me hice socio – dijo Antonio, radiante –; pero ¿por qué no lo afeitan?",
                    "Algunos lo hacen, como si pelaran un chancho, aunque no le cambia el gusto.",
                    "Pero debe quedar mucho más lindo de ver.",
                    "Para los remilgados – se rió Luis.",
                    "Terminaron el almuerzo cuando se anunciaba que iba a correrse la primera penca. Se dirigieron a las sendas y se ubicaron en la sentencia.",
                    "Hubo dos partidas erradas, pero en la tercera el juez bajó el pañuelo, se oyó el ¡se vinieron! y enseguida la polvareda, el griterío y el redoble de cascos a la disparada.",
                    "Pasaron como una luz por la sentencia, con el tostado ganando por amplio margen.",
                    "¡Tenías razón, tenías razón! – gritaba Antonio, palmeándole la espalda al padre de Luis –. Tenías que haberle apostado.",
                    "¿Y si perdía?",
                    "Una hora después se corrió la segunda penca, para enorme disfrute de los muchachos, pero la tercera no llegó a largarse porque poco después se concretó la amenaza del tiempo, descargándose un aguacero.",
                    "La gente se refugió en el boliche y en el galpón, mientras la lluvia arreciaba.",
                    "Cuando una hora después el chaparrón paró, la mayor parte del público aprovechó para irse. Unos diez a doce, entre otros el viejo Farías, hicieron rueda en torno al fogón que había en un extremo del galpón.",
                    "Pusieron sus calderas o latas de agua en el fuego y empezó a circular el mate.",
                    "El padre de Luis miró al grupo y le dijo a los muchachos, sonriendo: En ese lote están los tres o cuatro mayores mentirosos de Cañada Seca, uno de ellos es el viejo Farías.",
                    "¿Podemos sentarnos en la rueda? – preguntó Antonio.",
                    "Si, pero quédense callados y, sobre todo, no interrumpan al que está haciendo un cuento o narrando un sucedido, porque si le estropean el efecto, los mata.",
                    "Yo me llevo a mi mujer y a la nena a tomar algo al boliche, y cuando nos vayamos los vengo a buscar.",
                    "Calladitos, los dos se arrimaron a la rueda, tomaron dos trozos de tronco aserrado y se sentaron al lado y un poco atrás del viejo Farías.",
                    "Entre éste y un negro viejo, de mota casi blanca. Dos lugares más allá alguien estaba hablando, y los muchachos le prestaron atención.",
                    "Era un viejo también, de aspecto aindiado, que en ese momento terminaba de contar algo.",
                    "Y si no me creen – remató –, ahí está el finado Remigio Sosa que no me deja mentir.",
                    "Unos cuantos se rieron. El viejo Farías carraspeó, aclarándose la garganta para arrancar, pero le ganaron de mano y otro empezó un cuento de una pesquería.",
                    "Donde había sacado, después de una lucha detallada y homérica, una tararira gruesa como esta pierna.",
                    "Al terminar, el viejo Farías volvió a carraspear, pero esta vez levantó la mano, pidiendo atención, y arrancó:",
                    "Yo una vez – dijo, recorriendo todos con la mirada – crié una tararira guacha.",
                    "Hizo una pausa para concentrar la atención de los oyentes, y prosiguió:",
                    "Mire usted la casualidad. Venía de vuelta de una tropeada, llegando al rancho que tenía en los bajos del Sarandí.",
                    "El rancho estaba en el bajo, pero de lejos del arroyo y las crecientes. Pa lavarme un poco, fui con la palangana y el jarro hasta la orilla del agua.",
                    "Enllené el jarro y lo eché en la palangana. Y mire usted, ¿no va y sale del jarro una tararira chiquita, más corta que este dedo?",
                    "Oscurita estaba en la palangana blanca. Yo la miré, ¿y no va ella y me mira también?",
                    "Ahí nomás le tomé cariño, y ya mesmo resolví que la iba a criar guacha.",
                    "Hacía unos meses que una crucera que me había picado al Cabo, y el pobre perro se me murió hinchado.",
                    "Así que ahora, con la tararira, no iba a estar tan solo. Le puse de nombre Iracema, en recuerdo a una novia que tuve, y me llevé p'al rancho.",
                    "Se crió de mimosa, mire, que usted no sabe. Y era flor de bandida la Iracema, le gustaba esconderse y se mataba de risa si yo no la encontraba.",
                    "Eso sí, aparecía enseguida si yo le gritaba: Iracema, está la comida. Porque comer, comía, sabe, y se fue poniendo viciosa de grande.",
                    "Eso sí, delicada para comer. Cuando era chiquita le daba lombrices, después isocas y, cuando ya era grande, sapos.",
                    "Pero una vez que no pude encontrar ningún sapo, la vi como enojada. Y más ofendida se puso cuando me vio agarrar un plato y servirme un guisito carrero – de arroz y charque – que me había cocinado.",
                    "Pa convencerla, le alcancé una cucharada diciéndole ¿no ves que esto no te va a gustar?",
                    "Y mire usted, se me comió todo el guiso y el que se acostó con hambre fui yo. Y nunca más quiso comer sapos, así que desde entonces yo cocinada pa'los dos.",
                    "Ya tenía como tres años, y estaba hermosa, cuando se vinieron aquellas inundaciones machas del 59, ¿se acuerdan?",
                    "Llovió tanto que, por primera vez, la creciente rodeó el rancho. Cerré bien la puerta, puse chapas y latas para que el agua no se ganara adentro, y me acosté.",
                    "Al otro día de mañana, me asomé a la ventana y el agua tenía como un metro de altura contra la pared del rancho.",
                    "Vení, Iracema, venía a ver qué cosa imponente, le dije. Y, pa que pudiera ver, la alcé con los brazos y me asomé con ella a la ventana.",
                    "¡Pa qué lo habré hecho! La pobrecita se llevó tal susto al ver aquella inmensidad de agua, que se sacudió, se me resbaló, ¡y no va y se me cae al agua!",
                    "¡Qué desgracia! – terminó el viejo, y se quedó callado.",
                    "Antonio, impaciente, preguntó: ¿Pero qué pasó?",
                    "¿No te dije que la había criado guacha? ¡La pobrecita no sabía nadar y se me ahogó!",
                    "Hubo una carcajada general, pero el viejo Farías permaneció serio, impertérrito. Los miró a todos y sentenció:",
                    "Es la pura verdad – y quedó callado.",
                    "Antonio aprovechó para meter baza, queriendo oír la versión del viejo, de la luz mala del viernes de noche.",
                    "Cuente lo de la tapera del inglés – le dijo, pero el viejo se hizo el desentendido.",
                    "Lo que fue aprovechado por el negro de la mota blanca para intervenir.",
                    "La tapera del inglés es un lugar mal asombrado – dijo en un acento abrasilerado –. Yo sé algo de la historia porque me la contó Ña Remigia, que la conoce bien.",
                    "Lo que sé es que el inglés desapareció cuando el asalto de la estancia, en tiempos de la revolución del 97.",
                    "Un matrero que le decían Manduca ya había querido asaltar la estancia. La primera vez no tuvo suerte, pero después casi toda la gente que tenía el inglés se le fue con la revolución y la volvieron a asaltar.",
                    "Al inglés le habían quedado solo tres viejos, y quiso mandarlos a todos a la estancia de un amigo.",
                    "Dos fueron, llevando una carta que el inglés les dijo que era muy importante, cuando en realidad en la carta le pedía al amigo que no dejara volver a los viejos para que no los mataran.",
                    "Sólo uno no quiso ir – hizo una pausa y sonrió – ¡negro tenía que ser!",
                    "¿Y qué le pasó? – interrumpió Antonio.",
                    "El negro lo miró con severidad, tomó el mate que le pasaban, lo chupó largamente, lo devolvió y se acomodó para seguir.",
                    "El estanciero amigo juntó gente y salió a ayudar al inglés, pero llegó tarde.",
                    "En la madrugada, antes de aclarar, Manduca hizo que tiraran unos tiros para entretener al inglés y al negro, saltó el muro de atrás, sorprendió al negro y lo mató de una puñalada en la espalda.",
                    "Al oír el grito, el inglés que estaba en el mirador salió afuera, contra la luna, y ahí le pegaron un balazo.",
                    "Bueno… dicen que le pegaron, porque había manchas de sangre. Pero nunca más se volvió a ver al inglés.",
                    "La partida de Manduca esperó que aclarara y entró a la casa, rompieron una puerta, pero no había nadie.",
                    "Destrozaron todo buscando el oro que era fama que tenía el inglés, pero hallaron ni una onza.",
                    "Furiosos, le pegaron fuego a todo. Cuando la casa empezó a arder, levantó vuelo del techo una enorme águila mora, esa misma que hasta hoy vuela todos los días sobre la tapera.",
                    "Hay muchos que dicen – y yo les creo – que esa águila mora es el mismísimo inglés.",
                    "¿Y nunca lo encontraron? – preguntó Antonio.",
                    "No señor.",
                    "¿Y qué pasó con ese bandido de Manduca?",
                    "Shhh… – dijo el negro, llevándose el dedo a los labios y mirando hacia la puerta.",
                    "Acababa de entrar un hombre que caminó hacia ellos, pasó a su lado sin saludar a nadie y levantó un recado que estaba en un rincón del galpón.",
                    "Cuando pasó de vuelta, los muchachos vieron que tenía una larga cicatriz en la cara, desde la sien casi hasta el mentón.",
                    "Todos miraron pasar en silencio y, cuando salía, el negro habló:",
                    "Ese es el nieto de Manduca, y es de mala entraña. Ya tiene dos muertes por lo menos.",
                    "Hubo un silencio general que el viejo Farías aprovechó para arrancar con otra historia.",
                    "Yo de águilas sé poca cosa – dijo –, pero de tarariras sé una barbaridad.",
                    "Uno largó la risa. ¡Otro cuento de tarariras, Don Farías!",
                    "Pero los muchachos no llegaron a escucharlo, porque en ese momento entró el padre de Luis y les dijo que se iban."
                ]
            },
            {
                'nombre': 'Capítulo 7: La tapera del Inglés',
                'fondo': 'tapera',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Ya en las casas, les contaron a los otros el cuento que habían oído al viejo Farías.",
                    "El padre se reía: Yo les dije que el viejo era un gran mentiroso, de los mejores de Cañada Seca. Siempre está inventando historias fantásticas.",
                    "Le pedí que contara lo de la luz mala – dijo Antonio – pero otro hombre, que no sabía lo que no pasó el viernes, se puso a contar la historia del inglés.",
                    "¿Es verdad esa historia o todos eran mentirosos en aquella rueda?",
                    "¿Quién fue el que lo contó?",
                    "Un negro viejo, de pelo blanco.",
                    "¿Medio abrasilerado?",
                    "Sí.",
                    "Ese era el negro Sabino, que generalmente no inventa cosas. Repite a veces historias sobrenaturales que otros le cuentan, pero no tiene fama de mentiroso.",
                    "¿Qué fue lo que les contó? – y los muchachos le repitieron, lo más fielmente posible, lo que había dicho Sabino, incluyendo la llegada del hombre de la cicatriz.",
                    "Si – dijo el padre – esa es la misma historia que yo conozco como me la contaba mi abuelo. El inglés desapareció y nunca más se supo de él.",
                    "Después, primero le llevaron los ganados y, con el tiempo, le fueron ocupando las tierras; hubo, muchos años más tarde, un lote de juicios de prescripción y aquella estancia quedó repartida entre cerca de quince propietarios.",
                    "¿Cómo se llamaba el inglés?",
                    "El último, el que desapareció, se llamaba John Baker. Su padre, el que fundó la estancia, era Richard Baker, y ése era el verdadero inglés. El hijo era uruguayo.",
                    "¿Quién es Ña Remigia, que ese Sabino dijo que sabía toda bien la historia?",
                    "Es una vieja, medio bruja y medio loca, que tiene mucha fama y mucha clientela. Es la curandera más mentada de Cañada Seca, y vive en un rancho a unas cinco cuadras del camino que sale del pueblo y pasa por la tapera del inglés.",
                    "Y la tapera, ¿podemos visitarla? – preguntó Antonio, lleno de curiosidad.",
                    "Supongo que sí. Hoy el campo donde está la tapera es de los Zabala, amigos míos. Como la tapera está bien sobre el camino, no veo que haya problema en que aten los caballos en el alambrado y entren a mirarla.",
                    "¿Vamos mañana a verla? – propuso Antonio, entusiasmado.",
                    "¡Vamos! – dijo Luis.",
                    "Son dos leguas de ida y dos de vuelta – dijo el padre –, es decir veinte quilómetros. ¿Te parece que tus músculos hípicos no sufrirán mucho?",
                    "Creo que no – dijo Antonio sonriendo –, ya me duele poco.",
                    "Una preocupación le nubló el rostro: ¿De día no hay problema de luces malas?",
                    "No, ninguno. Vayan tranquilos.",
                    "Pero el día siguiente, y el otro día siguió lloviendo, de modo que se pasaron casi todo el tiempo en el galpón, ayudando al padre en esos trabajos que siempre se dejan para los días de lluvia.",
                    "Como había otros trabajos que hacer, recién el viernes se tomaron la mañana libre para ir hasta la tapera del inglés.",
                    "Es una hora al trote – dijo Luis, y allá marcharon.",
                    "Llegaron al pueblo, lo cruzaron y tomaron el camino que salía al otro lado. Era un camino de tierra, poco más de un trillo, sin poblaciones cercanas.",
                    "El camino primero bajaba una larga ladera, seguía un trecho de escasas ondulaciones y luego venía la aún más larga ladera hacia la cumbre donde estaba la tapera.",
                    "Vieron, a mitad del camino, hacia la izquierda, un rancho que – por lo dicho por el padre – tenía que ser el de Ña Remigia, pero a la distancia que pasaron no pudieron apreciar nada.",
                    "Cuando empezaron la larga subida, y aunque la había visto el día que fueron de pesca, Antonio volvió a impresionarse con el tamaño de la tapera.",
                    "Llegaron a ella, ataron los caballos y se bajaron. Desde ese lugar se dominaba el paisaje hasta una distancia considerable en todas las direcciones.",
                    "¡Qué lugar bárbaro eligieron! – exclamó Antonio.",
                    "El perímetro del casco, de más de media hectárea, estaba rodeado enteramente por un cerco de piedra, bastante más alto que los cercos comunes.",
                    "Le llegaba a los muchachos por el hombro en los lugares en que estaba intacto. En muchas partes estaba derruido, en buena medida por talas y coronillas que habían crecido protegidos por él.",
                    "Entraron con cierta aprensión, recordando el susto de la noche del viernes. Cautelosamente, se acercaron al arbusto donde había estado la luz mala y lo observaron detenidamente.",
                    "No había el menor rastro del fenómeno, ni siquiera una hojita quemada. Respiraron aliviados y siguieron.",
                    "Dentro del recinto había varias construcciones en diversos grados de deterioro. En general, sólo quedaban los muros exteriores de piedra.",
                    "La construcción principal, obviamente la casa del dueño, llamaba la atención por su tamaño. Era enorme, en forma de L, y en algunas pocas ventanas conservaba las gruesas rejas de hierro.",
                    "De marcos, postigos y puertas no quedaba nada, como tampoco de los techos. En la esquina de la casa, arriba, estaban las ruinas de lo que había sido un mirador.",
                    "Aunque más que mirador parecía la garita de guardia de una fortaleza, con ventanitas estrechas, como para disparar un arma estando protegido.",
                    "Sólo quedaban dos paredes del mirador, las que estaban a plomo con la esquina de la casa.",
                    "Cuando se acercaron a ella y entraron por lo que debió de haber sido la puerta principal, vieron que en el ángulo, debajo del mirador, había – en bastante buen estado – una escalera de caracol de hierro fundido.",
                    "El piso estaba cubierto de escombros de los techos derrumbados y de algunas paredes internas de ladrillo que también habían caído.",
                    "Otras se mantenían en pie, con aberturas sin marcos ni puertas. Varias lagartijas corrieron cuando los muchachos entraron, escondiéndose entre los escombros.",
                    "¡Ojo con las víboras! – advirtió Luis –. Fíjate donde pisás.",
                    "Las paredes estaban ennegrecidas, sin que pudieran saber si era por el incendio que la destruyó o por el simple paso de los años.",
                    "La habitación era enorme, ocupando todo el lado corto de la L. Antonio, mirando en derredor, comentó: ¡Qué lo tiró que es grande! El apartamento nuestro debe caber dos veces en esta pieza.",
                    "En la pared opuesta a la que ocupaba la escalera de caracol, había una enorme estufa de leña, de cuya chimenea sólo quedaba el principio.",
                    "Yuyos y arbustos crecían en muchos lados, incluso una palmera levantaba su copa varios metros por encima de los muros.",
                    "Caminando con cuidado sobre los escombros, Antonio se acercó a la estufa. Ésta también estaba construida en piedra.",
                    "La repisa del hogar era un enorme pedazo de granito rosado, bien trabajado y sin pulir, sobre el que se apoyaba lo que quedaba de la chimenea.",
                    "Tenía muchos líquenes adheridos, estaba sucio como el polvo en otros lados, o tal vez era sólo la pátina del tiempo.",
                    "El extremo izquierdo era el que estaba más limpio, y observó allí unos puntitos, unos agujeritos que parecían formar una letra P.",
                    "Lo miró mejor y le pareció que no, y lo iba a llamar a Luis cuando fue éste el que lo llamó:",
                    "Mirá lo que agarré – y le mostraba el puño cerrado.",
                    "Fue hasta él, preguntándole qué era y Luis, sin abrir el puño, le dijo que era un pichón de lagartija, chiquito.",
                    "¿Qué vas a hacer con él?",
                    "Soltarlo. Estos bichitos son útiles, se alimentan de insectos. Pero quería que lo vieras.",
                    "Agachándose, puso el puño en el suelo, con los dedos hacia arriba, y abrió la mano. Antonio se puso a reír, porque el bichito no tenía más de cinco centímetros y salió como una luz, desapareciendo bajo los escombros.",
                    "Vení por aquí – dijo Luis, y empezaron a recorrer la sucesión de habitaciones que habían constituido el brazo largo de la L.",
                    "De la última, salieron afuera. Después venía un pozo con brocal de piedra, otra construcción larga, de varias piezas, que debió haber sido casa y cocina de peones.",
                    "Otra más pequeña, que conservaba dos paredes interiores – tal vez la casa del capataz – y lo que obviamente había sido el galpón de la estancia.",
                    "Una construcción muy grande – casi como la casa – que debió tenido techo a dos aguas – y no se azotea, como el resto – porque las paredes laterales eran bajas mientras que la del frente y la del fondo eran de mojinete.",
                    "¡Qué imponente! – dijo Antonio. ¡Lo que debió haber sido esto!",
                    "Empezaron a recorrer el perímetro, mirando algunos añorosos coronillas y un más viejo y gigantesco ombú, cuya sombra abarcaba un área enorme.",
                    "Llegaron a lo que debió haber sido la única entrada del recinto, donde dos gruesos y altos postes de piedra marcaban la abertura. Allí debió habido un portón.",
                    "Cansados de la recorrida, se sentaron en una piedra larga y cilíndrica que estaba afuera, contra el muro que le servía de respaldo.",
                    "Luis empezó a revisar, entre sus piernas, las rayas y vetas que tenía la piedra y comentó:",
                    "Este debe haber sido el banco del inglés, para sentarse a mirar sus tierras.",
                    "Permanecieron un rato en silencio. A pesar del soleado día de invierno, la tapera tenía algo de lúgubre.",
                    "Sin que se dieran cuenta, la tristeza y la melancolía del lugar los había ido invadiendo. Los dos se miraron:",
                    "¿Nos vamos?",
                    "Y tomaron el camino de regreso al tranco lerdo, como sin ganas de trotar.",
                    "Cuando habían andado unos quinientos metros, se cruzaron con un hombre que venía a caballo por el camino. Era el hombre de la cicatriz, el nieto de Manduca.",
                    "Buenos días – dijo Luis, pero el hombre apenas respondió con un gruñido.",
                    "Cumplido, el hombre – comentó Antonio, cuando se habían alejado un poco.",
                    "Pero, si se hubieran dado vuelta, habrían visto al hombre de la cicatriz con el caballo detenido y observándolos atentamente."
                ]
            },
            {
                'nombre': 'Capítulo 8: Visita a la curandera',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Esa noche, después de cenar, Antonio le comentó a Luis:",
                    "¿Sabes que me gustaría ir de nuevo a la tapera?",
                    "Primero me pareció que sí, después que no, y ahora me parece de nuevo que sí, que hay algo escrito en la estufa de leña.",
                    "¿Por qué no me lo mostraste?",
                    "Te iba a llamar cuando me llamaste vos por la lagartija chiquita, y después se me pasó.",
                    "¿Y qué había?",
                    "Parecía haber una letra, pero estaba sucio y con líquenes. La próxima vez que vayamos miramos bien.",
                    "Será en las próximas vacaciones, porque mañana ya quedamos de ir al pueblo temprano, con el tractor y la zorra, a traer bolsas de ración: de tarde vamos al campo de mi tío, y pasado mañana nos vamos.",
                    "El domingo, el padre, la madre, la hermanita y ellos fueron en la camioneta al pueblo, donde se embarcarían de regreso a Montevideo y a las clases.",
                    "Al despedirse, el padre de Luis dijo a Antonio: Fue muy lindo tenerte aquí, y me ayudaste mucho. ¿Cuándo volvés?",
                    "Cuando me inviten – dijo Antonio, contento.",
                    "La casa está abierta para cuando quiera venir.",
                    "Entonces en setiembre, en las vacaciones de primavera.",
                    "Te vamos a estar esperando.",
                    "Ya en Montevideo, casi quedó afónico contando en su casa todas las experiencias que había vivido, las cosas que había aprendido, las aventuras y los paseos.",
                    "¿Y Luis no se reía de tus chapetonadas? – le preguntó el padre.",
                    "No. Me enseñaba como hacer las cosas.",
                    "¿Viste? Cada uno en su medio puede ser solidario. O puede ser egoísta y crítico. Me alegro que se entiendan así.",
                    "En el liceo y en club de deportes, Antonio les contó a los demás amigos, en detalle, todo lo que había vivido en aquellas dos semanas de campo.",
                    "Haciendo que el ya montevideanizado Luis subiera en la estima de todos.",
                    "¿Aprendiste a andar a caballo?",
                    "Bastante. Por lo menos ahora ni me caigo ni me pelo, que ya es mucho. Pero como voy a volver, ya van a ver qué jinete.",
                    "Hopalong Cassidy – le dijo uno de ellos, y todos se rieron.",
                    "Entre las clases, los estudios, las actividades deportivas, el teatro de los viernes y los bailes de fin de semana, los siguientes dos meses pasaron relativamente rápido.",
                    "Y un tibio sábado de primavera se encontraron los dos sentados en un ómnibus rumbo a Cañada Seca.",
                    "Antonio sintió el placer de volver a ese lugar al que se sentía familiar y con el que se había encariñado. Era así como volver a casa después de una ausencia.",
                    "Al otro día había de nuevo pencas en aquel almacén y volvieron a ir los cinco, pero esta vez Antonio miraba todo con aire de conocedor. Hasta opinó sobre los parejeros.",
                    "Desde que llegaron se habían propuesto ir a la tapera del inglés, pero el padre, que estaba con un peón enfermo, les pidió que recorrieran de mañana y de tarde el potrero donde una majada de ovejas Romney estaba terminando la parición.",
                    "Se encarneraron en la segunda quincena de marzo, y aunque el grueso ya parió, queda un lote de parición tardía.",
                    "De modo que el lunes ensillaron la yegua zaina de Luis y el bayo que usaba Antonio y se dirigieron al potrero de las ovejas.",
                    "Entraron al potrero, y mientras Luis cerraba la portera de cimba, Antonio enfiló al trote hacia las ovejas.",
                    "¡Párate! – le gritó Luis y, y subiendo a su yegua, lo alcanzó, explicándole:",
                    "No cruces por ahí, y menos al trote. No hay que alborotar la majada que está pariendo, porque los corderitos chicos pueden extraviarse de la madre.",
                    "Vamos despacito, al tranco y rodeándolas. Si vemos alguna mal echada, que no se puede parar, o con el cordero atracado, entonces nos bajamos y la ayudamos.",
                    "Antonio miraba con un placer mezclado con ternura a los corderos más chicos, aquellos amarillos acabados de nacer y los muy blancos, recién lamidos por sus madres.",
                    "Cómo miró divertido a un pichón de terutero, pura pata, que se levantó y empezó a correr hasta que, echándose de nuevo, desapareció en el pasto.",
                    "Estuvieron tres días en ese trabajo, que tenía mucho más de placer: dos recorridas de mañana y dos de tarde, hasta que se recuperó el peón que lo tenía a su cargo.",
                    "Entonces sí, resolvieron ir al otro día a la tapera del inglés.",
                    "Cuando el jueves de mañana estaba por partir, Luis trajo una bolsita de lona que ató a los tientos, y explicó:",
                    "Llevo una botella con nafta, un trapo y un cepillo de alambre. Vos dijiste que aquello estaba sucio.",
                    "Cierto – dijo Antonio –; fíjate si tenés también una tiza.",
                    "Cuando llegaron fueron derecho a la estufa de leña y allí, en la gruesa repisa de granito, Antonio le mostró lo que había visto.",
                    "¿No te parece que estos pocitos forman un P?",
                    "Si – dijo Luis y, sacando el cepillo de alambre, limpió el frente de líquenes y tierra.",
                    "Después, empapó el trapo en la nafta y frotó la superficie. Aparecieron entonces una cantidad de pocitos en todo el frente de la estufa.",
                    "¡Esto es algo escrito! – dijo Luis, entusiasmado.",
                    "Fíjate, aquí hay restos de pintura – señaló Antonio con el dedo.",
                    "Y la primera letra es una R, no una P.",
                    "Antonio tomó entonces la tiza y, con cuidado, fue uniendo los pocitos con un trazo.",
                    "A medida que se iban formando las letras, más emoción sentía, hasta hacerle temblar la mano.",
                    "Cuando concluyó, en grandes letras mayúsculas, se podía leer: READ THE BIBLE.",
                    "Lee la Biblia – tradujo Antonio, un poco desilusionado –. Esto más bien parece propaganda de los mormones.",
                    "Se quedaron un rato observándolo. Después Antonio volvió a mojar el trapo y quitó los trazos de tiza.",
                    "Con el granito aún mojado, le tiró unos puñados de tierra.",
                    "Por si las moscas – dijo.",
                    "Salieron de allí, montaron sus caballos y llegaron a las casas justo para el almuerzo.",
                    "Esa noche, solos en el cuarto, el texto escrito en la chimenea seguía dándoles vuelta en la cabeza.",
                    "Sólo que fuera gente muy creyente – dijo Antonio.",
                    "No – dijo Luis –, hay una cosa que no encaja.",
                    "¿Cuál?",
                    "Que ese cartel fue pintado. Esa gente era muy rica. Si hubiera querido poner una leyenda así, lo habrían hecho tallar en la piedra, en relieve.",
                    "¡Cierto! Y eso está hecho a lo bandido. Las letras no son parejas Parece que lo hubieran pintado a la que te criaste y después le hubieran hecho las marcas con un clavo.",
                    "Un punzón, más bien.",
                    "¿Será algún mensaje del inglés?",
                    "No sé.",
                    "Luis pensó un poco y agregó:",
                    "¿Por qué no vamos mañana a hablar con la curandera? El negro Sabino dijo que ella sabía toda la historia.",
                    "Pero no le decimos nada del cartel.",
                    "Al otro día, de mañana, volvieron a emprender el camino al pueblo y siguieron, al otro lado, el trillo que habían recorrido en la víspera.",
                    "El campo estaba lindo. Había llovido bien y la primavera empujaba con fuerza. Las laderas se venían cubriendo de una pelusa verde, como una barba de diez días.",
                    "Doblaron en la entrada del rancho de la curandera y anduvieron unos quince metros hasta llegar a él.",
                    "El rancho era decrépito, vencido. A su lado una vieja higuera, con el amago de futuras brevas, protegía con la sombra densa de sus hojas ásperas a un barril de agua sentado en un rastrón.",
                    "En dos latas, a cada lado de la puerta, había malvones aún sin flor.",
                    "No te bajes hasta que ella lo diga – advirtió Luis, y golpeó las manos.",
                    "Pasaron dos minutos y nadie apareció. Luis volvió a llamar y de adentro del rancho se oyó:",
                    "¡Momento! Ya voy – y segundos después se asomó a la puerta la imagen de bruja más real que Antonio había visto en su vida.",
                    "Era vieja, pero vieja de verdad, encorvada y arrugada, con un pelo largo, sucio y greñudo, y un vestido de color indefinido que le colgaba hasta el suelo.",
                    "Los observó con unos ojitos oscuros y les dijo:",
                    "¡Abájensen!",
                    "Desmontaron los dos, ataron sus caballos a la higuera y se acercaron al extraño personaje.",
                    "Buenos días, señora – dijo Luis –; veníamos a verla porque…",
                    "Si andan buscando una vencedura hoy no puedo. Estoy preparando un cocimiento y tengo que salir a buscar unos yuyos. Así que vengan mañana.",
                    "No señora, no es nada de eso. Queríamos hablarle porque dicen que usted es la que sabe más de la historia del inglés, el de la tapera que está allá arriba.",
                    "Ña Remigia los miró con sorpresa y abrió la boca en una sonrisa vacía de dientes.",
                    "Entró al rancho, salió con un banquito y se sentó, indicándoles que hicieran lo mismo en un tronco que estaba enfrente.",
                    "Si es pa hablar del inglés, tengo tiempo. Yo siempre tuve tiempo pa el inglés, y eso que él a veces me judiaba.",
                    "¿A usted, Ña Remigia? – preguntó Antonio.",
                    "Si a mí. El inglés era divertido, pero también sabía ser diablo cuando quería. Y me discutía de magia y de religión.",
                    "Él insistía en que las cosas que yo hago por los poderes que tengo, eran en realidad ordenadas por Dios. Yo me reía – clavó sus ojillos en los dos muchachos.",
                    "¡Si ustedes supieran!",
                    "Antonio sintió un estremecimiento y dio gracias mentalmente por estar fuera del rancho. Juntó coraje y planteó la duda que sentía:",
                    "Pero señora, eso tendría que haber sido como hace cien años. ¿No habrá sido su abuela la que conoció al inglés?",
                    "Los ojos de la curandera brillaron intensamente negros y lo miró con una expresión dura.",
                    "¡Cien años! ¿Y qué es el tiempo? ¿Qué sabés vos del tiempo? ¿Qué sabés de los poderes que hay?",
                    "Antonio balbuceó una disculpa y se calló, asustado. La vieja tomó con la mano los collares que pendían de su pescuezo, se balanceó suavemente hacia ambos lados.",
                    "Y, mientras murmuraba algo ininteligible, sus ojos parecieron mirar hacia adentro.",
                    "De repente echó la cabeza hacia atrás y lanzó otra carcajada estridente.",
                    "¡Éste inglés! Si me hubiera hecho caso y me hubiera traído algo de ella, yo le hubiera hecho una vencedura infalible para su mujer.",
                    "Pero él llamó al médico – y Ña Remigia escupió con rabia en el suelo –. ¡Yo le dije! Le dije que así ella se iba a morir. Y se murió nomás.",
                    "Pero él seguía creyendo en el médico, en los rezos y en la Biblia.",
                    "Antonio y Luis se miraron, alertas.",
                    "¿Qué Biblia, Ña Remigia?",
                    "La de él. La que tenía allá – y señaló rumbo a la tapera. Soltó otra risa y agregó:",
                    "Si ahora anda como ánima en pena, es culpa de él.",
                    "¿La luz mala es el inglés?",
                    "¿Y quién va a ser?",
                    "No sé. Está eso que dicen del águila mora. Hoy la vimos.",
                    "También. El inglés es bien capaz de ser águila de día y luz mala de noche – y volvió a reírse como si hubiera dicho algo muy gracioso.",
                    "Ña Remigia – terció Antonio, queriendo volver al tema que los había traído –, esa Biblia del inglés, ¿usted sabe dónde está?",
                    "La vieja lo miró con aire de sospecha:",
                    "¿Pa qué querés la Biblia?",
                    "Para verla, debe ser muy antigua.",
                    "Era muy vieja, sí. Y yo la quería pa mí. No pa leerla, que no sé, pero tenía unas estampas muy lindas, en colores, que me gustaban pa colgar en el rancho.",
                    "Le pedí muchas veces, y él no quería arrancar ninguna.",
                    "Sólo la última vez que lo vi, que venía con la Biblia, arrancó una y me la dio. Pero, ¿no va la mala suerte que un día se desprendió, cayó arriba del fogón y se quemó?",
                    "Quedó callada, la mente sumida quien sabe en qué.",
                    "Señora – dijo Luis, suavemente –, ¿cuándo fue que vino con la Biblia y le regaló la estampa?",
                    "La curandera volvió lentamente a él, como quien sale de un profundo pozo de recuerdos.",
                    "Venía a caballo, con la Biblia bajo el brazo. Ni se bajó, le arrancó la estampa y siguió rumbo al pueblo. Nunca más lo vi.",
                    "A los días asaltaron la estancia y no se supo más de él. En la noche de San Juan, fue. ¡Ese inglés! ¡Mire que andar a los tiros en lugar de prender fogatas esa noche!",
                    "Y empezó a sacudirse de tanto que se reía.",
                    "Los muchachos se pararon, se despidieron y se fueron.",
                    "Cuando retomaron el camino pasó sobre ellos, solitaria y veloz, el águila mora."
                ]
            },
            {
                'nombre': 'Capítulo 9: La botella enterrada',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Esta vez el conciliábulo fue a caballo, a lo largo de la media legua que el rancho de Ña Remigia distaba del pueblo.",
                    "Los muchachos venían excitados, como en ascuas, por la historia de la curandera. Al mismo tiempo desconfiaban de ella.",
                    "Tu padre tenía razón – decía Antonio –, esa vieja está rechiflada.",
                    "Más loca que gallina atada de la cola – apoyaba Luis. ¿Cómo va a decir que conocía al inglés hace un siglo? Se debe estar creyendo las historias que oyó.",
                    "¿Y si lo conoció? – casi susurró Luis.",
                    "Antonio lo miró fijo. ¡Vos creés?",
                    "No sé, no sé qué creer.",
                    "Antonio pensó un poco. Sonrió y dijo:",
                    "Bueno, ¿te acordás de la clase de filosofía? ¿Del principio del tercero excluido? Aquí hay solo dos posibilidades: lo que dice la vieja es mentira, o lo que dice la vieja es verdad.",
                    "Cierto.",
                    "Entonces, ¿qué perdemos si suponemos que es verdad y seguimos averiguando?",
                    "Nada. Lo peor que puede pasar es que al seguir averiguando, descubramos que era mentira. Pero aún así, nos vamos a divertir jugando a los detectives. ¿De acuerdo?",
                    "De acuerdo. Vamos a arrancar suponiendo que es verdad. ¿Quién empieza?",
                    "¡Yo! – dijo Luis –, porque ya venía pensándolo. Fíjate una cosa, Antonio, lo que contó Ña Remigia es coherente con el texto que encontramos en la estufa.",
                    "Y entonces el Leé la Biblia se transforma en una clave. Quiere decir que el inglés la puso ahí para que buscáramos la Biblia. Esa Biblia.",
                    "O sea – siguió Antonio – algo debe tener la Biblia que el inglés quería que viéramos. Que el que encontrara el cartel y se diera cuenta de que era un montaje y no una propaganda religiosa, saliera a buscar la Biblia del inglés, no cualquier Biblia.",
                    "¡Justo! Y entonces es lógico que, en previsión de que la estancia fuera asaltada, se la llevara a un lugar seguro.",
                    "Al pueblo. ¿Pero dónde en el pueblo?",
                    "Yo diría que en la iglesia – dijo Luis –; ¿no es el mejor lugar para una Biblia? Además, si quería que la encontráramos, tiene que estar en un lugar así. No la iba a esconder donde nadie la encontrara.",
                    "Entonces, ¡a la iglesia! – dijo Antonio, y arrancó al galope.",
                    "Llegaron a la capilla del pueblo, se bajaron y entraron casi corriendo. Estaba vacía, golpearon en la sacristía y apareció el cura.",
                    "Dígame, padre, ¿tiene alguna Biblia?",
                    "Claro tengo tres.",
                    "¿Podemos verlas?",
                    "El cura los hizo entrar y les mostró tres libros de tamaño medio, de tapas negras.",
                    "¿Son antiguas, padre?",
                    "A ver – dijo el cura y las revisó –; ésta es de 1927, ésta es de 1980 y ésta de 1963.",
                    "No padre, éstas no. Buscábamos una Biblia vieja, del siglo pasado.",
                    "No – dijo el cura –, no hay ninguna.",
                    "Tal vez en inglés.",
                    "¡Jamás! Aquí solo entran las Biblias de la Santa Iglesia Católica Apostólica Romana – y puso cara de enojado.",
                    "Ya en la calle, miraron alrededor y se miraron.",
                    "¡Yo estaba tan seguro! – dijo Antonio –. ¿Y ahora?",
                    "Quedan dos posibilidades: la comisaría y la escuela.",
                    "Fueron hasta la escuela y la encontraron cerrada. Golpearon en la casa de la maestra y no salió nadie.",
                    "Una vecina se asomó y les dijo:",
                    "La maestra no está. Se fue de vacaciones.",
                    "¡Igual que nosotros, de vacaciones! – se lamentó Antonio.",
                    "Dijo que volvía el sábado de tarde o el domingo de mañana. Las clases empiezan el lunes.",
                    "Las nuestras también. Muchas gracias, señora.",
                    "Encaminaron sus pasos a la comisaría y allí repitieron la misma pregunta a un sargento gordo y panzón.",
                    "¿Biblia? Le erraron, muchachos, vayan a la iglesia. Aquí solo tenemos el reglamento.",
                    "Subieron a sus caballos y volvieron al campo, a esperar el retorno de la maestra.",
                    "Regresaron el sábado al pueblo y no había vuelto. Sacaron sus pasajes a Montevideo para el domingo de tarde y, en la mañana de ese día, fueron otra vez a caballo hasta la escuela.",
                    "Con alegría, vieron que la puerta de la casa estaba abierta. La maestra había llegado.",
                    "Era una muchacha joven que los atendió con cordialidad, más al saber que Luis había estudiado allí.",
                    "Cuando le preguntaron si en la escuela había alguna Biblia antigua, respondió:",
                    "Sí, ¿Cómo saben? Es la joya que tenemos en la escuela, porque es muy antigua. Se las regaló un inglés a la primera maestra que hubo aquí.",
                    "¿Podemos verla?",
                    "Vengan. Está en la escuela.",
                    "Abrió el local, los llevó a una piecita con un escritorio, que era La Dirección y de un cajón con llave sacó una caja de madera.",
                    "Abrió la caja y vieron un libro de grandes dimensiones en cuya tapa de cuero viejo decía en letras de oro THE HOLY BIBLE.",
                    "¿Podemos mirarla?",
                    "Con mucho cuidado. Es una reliquia de mil seiscientos.",
                    "Ella misma la sacó de la caja, la puso sobre el escritorio y la abrió.",
                    "Los muchachos no estaban en condiciones de apreciar una joya bibliográfica, pero igual se asombraron con el libro.",
                    "En las hojas en blanco que había al principio, se veían muchas anotaciones en caligrafías antiguas, muchas de ellas casi ilegibles.",
                    "Antonio leyó algunas con dificultad, y las fue traduciendo. Eran anotaciones, en inglés, de nacimientos, casamientos y muertes de la familia Baker a través de los años.",
                    "¿Podemos ver el final?",
                    "La maestra cerró el libro, lo dio vuelta y lo abrió por la tapa posterior.",
                    "En la última página había tres anotaciones. La primera mencionaba el nacimiento de John Baker en 1847.",
                    "La segunda, su casamiento en 1874, y la tercera, que era la más extensa, era una poesía en inglés firmada por el propio John Baker.",
                    "¿Me presta un papel y un lápiz? – pidió Antonio y, temblando, copió íntegro el último texto.",
                    "Al mismo tiempo pensaba aceleradamente qué explicación darle a la maestra si preguntaba y, cuando devolvió el lápiz y se guardó el papel, ella preguntó:",
                    "¿Qué es lo que están buscando en la Biblia?",
                    "El abuelo de mi madre era primo del inglés – mintió Antonio – y ella quería saber anotaciones sobre su rama de la familia. No vi nada, pero le copié lo último para ver si sirve.",
                    "La maestra quedó conforme con la explicación y, después de agradecerle lo amable que había sido, se marcharon.",
                    "¿Qué decía? – Preguntó Luis en cuanto salieron –. Tu inglés es mejor que el mío.",
                    "Es una clave, una pista que dejó el inglés.",
                    "¿De qué?",
                    "De una botella. Cuando lleguemos lo paso en limpio y lo traduzco.",
                    "Cuando llegaron a las casas, lo escribió con buena letra en una hoja de papel. El verso decía:",
                    "It's long time dead And will not rot You can put fire And burn will not",
                    "If you find it You'll find the spot.",
                    "Walk fifty yards At twelve o'clock Towards the sun (or straight North)",
                    "And dig the bottle Behind the rock.",
                    "Después tomó otra hoja y fue escribiendo la traducción, una traducción literal, sin buscar la rima:",
                    "Está muerto hace mucho Y no se pudrirá Podés ponerle fuego Y no se quemará",
                    "Si lo encontrás Hallarás el lugar.",
                    "Caminá cincuenta yardas A las doce en punto rumbo al sol (o derecho al Norte)",
                    "Y escarbá la botella Detrás de la roca.",
                    "Apenas terminó de escribirla los llamaron a almorzar, y concluido el almuerzo fueron a juntar sus cosas para emprender el viaje.",
                    "Antonio le dio a Luis la versión en español y guardó en su bolsillo la copia en inglés.",
                    "Lo estudiaremos en el ómnibus – le dijo.",
                    "Pero en el ómnibus hay mucha gente y no querían que los oyeran. Se pasaron gran parte del viaje leyendo y releyendo el verso del inglés.",
                    "¿Cuánto son cincuenta yardas? – preguntó Luis.",
                    "Antonio sacó una agenda, la consultó. Hizo un rápido cálculo mental y contestó:",
                    "Unos cuarenta y cinco metros.",
                    "¿Medidos desde dónde? – suspiró Luis.",
                    "Cuando llegaron a Montevideo, ninguno fue a su casa. Se sentaron en un banco de la Plaza Independencia y estuvieron largo rato dándole vueltas al asunto.",
                    "Era nomás como decíamos – dijo Antonio –; el inglés dejó un mensaje para que encontráramos algo que enterró.",
                    "Una botella, pero ¿qué puede haber en una botella?",
                    "No debe ser whisky – dijo Antonio riendo –, debe ser una carta, un testamento, algo que quedaría protegido por estar dentro de una botella.",
                    "Una botella, que está enterrada, atrás de una piedra, a cincuenta yardas… ¿de qué?",
                    "Eso es lo que tenemos que descifrar.",
                    "En los días siguientes siguieron y siguieron en inútiles especulaciones, sin lograr avanzar un chiquito.",
                    "Y, como sucede a menudo con las cosas insolubles, lo fueron gradualmente postergando en la memoria, sin olvidarlo pero echándolo cada vez más atrás.",
                    "Dejándose absorber por las cosas inmediatas.",
                    "Terminó setiembre y pasó octubre con un solo hecho destacado: el cumpleaños de Antonio el 24 de ese mes.",
                    "La madre de Luis había hablado con la suya y, para su alegría, recibió dos regalos que se complementaban: de sus padres, un par de botas negras, de caña blanda.",
                    "Y, de los de Luis, una bombacha también negra, bien criolla, hecha por la mejor modista de Cañada Seca.",
                    "Quedó muerto de ganas de poder estrenararlas.",
                    "Noviembre siguió sin novedades. La única fue que el 20 le llegó el turno a Luis de cumplir dieciséis años.",
                    "Caía sábado y se fue a pasarlo con sus padres, con precisas recomendaciones y exigencias de Antonio de que, sin él, no hiciera investigaciones por su cuenta.",
                    "Lo haremos los dos cuando terminen las clases. ¿Ta? – y se dieron la mano.",
                    "El día antes le habían hecho una fiestita de cumpleaños en lo de Antonio, con tres o cuatro amigos más.",
                    "Y la familia le regaló un cuchillo antiguo, con vaina de cuero y mango de plata y oro que el padre había encontrado en la feria de Tristán Narvaja.",
                    "Tenés que encontrar otro para mí – le dijo Antonio a su padre, con un poco de envidia.",
                    "¿Lo cambiarías por las botas?",
                    "No, jamás.",
                    "Entonces espera al año que viene.",
                    "Llegó diciembre y se acercaba el fin de cursos, que sería en quince días.",
                    "En la última semana de clases, el profesor de historia Natural llevó al aula una caja dividida en compartimentos, conteniendo distintos minerales.",
                    "Empezó a sacar piedras y a mostrarlas, explicando qué eran. Así habló de granitos, pegmatitas, filitas, basaltos, gneiss, esquistos.",
                    "De sus orígenes y los lugares del país donde eran frecuentes.",
                    "Tomó al final una piedra y se la alcanzó al que estaba más adelante.",
                    "Para ti, ¿esto es una piedra? – le preguntó.",
                    "Sí.",
                    "Ahora lo es, por la acción mineralizadora de algunos ríos del Uruguay. Pero esto no siempre fue piedra. Esto tuvo vida, fue madera.",
                    "Lo que tenés en la mano es un pedazo de tronco petrificado.",
                    "Se oyó una exclamación, Luis saltó de su asiento y salió corriendo del salón de clase.",
                    "Al verlo, Antonio se paró y salió tras él, sordo a los gritos del profesor.",
                    "Un adscripto los quiso detener en el patio pero ellos siguieron y salieron puerta afuera.",
                    "En la calle, Luis se detuvo de golpe y abrazó a Antonio vociferando:",
                    "¡Estaba ahí, estaba ahí, en las narices!",
                    "¿Qué cosa?",
                    "¡Yo le estuve mirando las vetas y los nudos!",
                    "¿A qué?",
                    "¡Al banco del inglés! Donde estuvimos sentados, recostados al muro. ¿No te acordás? No era una piedra, yo lo vi. ¡Era un tronco petrificado!",
                    "Antonio abrió una enorme boca de asombro.",
                    "Cuando consiguió cerrarla dijo:",
                    "Está muerto hace mucho, y no se pudrirá",
                    "Podés ponerle fuego y no se quemará –completó Luis –. ¿Te das cuenta? ¡La botella está enterrada a cincuenta yardas del banco del inglés!"
                ]
            },
            {
                'nombre': 'Capítulo 10: La carta de John Baker',
                'fondo': 'tapera',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Los pocos días que faltaban para la finalización de las clases les resultaron una condena, especialmente el concentrarse para algunas pruebas finales.",
                    "Pero las hicieron y las aprobaron con buenas calificaciones.",
                    "El tema era la botella, siempre la botella, sólo la botella. No quisieron contar a nadie lo que tenían entre manos hasta saber qué era realmente.",
                    "Pensaron que los amigos hasta se podrían reír de ellos, viéndolos ansiosos por una botella de fines del Siglo XIX.",
                    "En una ocasión Antonio preguntó:",
                    "¿A vos te queda claro eso de a las doce rumbo al sol y la aclaración derecho al Norte?",
                    "Sí, claro. A mediodía el sol está en el cenit, y lo tenés exactamente al Norte. Si clavás un palito en el suelo, la sombra es una línea Norte-Sur. Pero tiene que ser el mediodía meridiano.",
                    "Eso es la mitad del día. ¿Pero cómo se sabe?",
                    "Mirá: si el sol, por ejemplo, sale a las seis y se pone a las ocho, tenés catorce horas de luz. La mitad es siete, se lo sumás a las seis y te da la una de la tarde.",
                    "Para el inglés a las doce rumbo al sol era sinónimo de derecho al Norte. Hoy creo que no. Sin ir más lejos, hace poco adelantaron la hora, o sea que tendríamos que ver en el diario cuándo sale y cuándo se pone el sol y hacer los cálculos.",
                    "Cierto – dijo Antonio –, tal vez en la época del inglés los gobiernos no jorobaban con la hora.",
                    "Igual es fácil.",
                    "Hay otra cosa más fácil que dividir, y sumar, y andar clavando palitos.",
                    "¿Cuál?",
                    "Me llevo la brújula.",
                    "Cuando Antonio anunció en su casa que terminaban las clases y al otro día estaba en Cañada Seca, no causó mayor sorpresa.",
                    "Más bien estaban esperando eso, pero le hicieron prometer que el 23 de diciembre volvería para pasar Navidad con su familia.",
                    "¿No puede ser el veinticuatro?",
                    "Tenés que ayudar un poco. Hay que hacer compras, preparar cosas, no podés llegar a último momento.",
                    "Está bien. Prometido.",
                    "Llegaron de tardecita al campo, sin tiempo para salir, pero al otro día, cuando estaba aclarando ya iban al trote rumbo a la tapera del inglés.",
                    "Antonio iba sentado sobre una pala y Luis sobre un pico.",
                    "Se bajaron, ataron los caballos y se acercaron a lo que habían llamado el banco del inglés.",
                    "Ahí está el tronco petrificado – dijo Luis.",
                    "Era un trozo cilíndrico, de más de un metro y medio de largo y de grueso diámetro, en el cual se notaban vetas y nudos.",
                    "¿No lo habrá movido alguien? – preguntó Antonio.",
                    "Intenta moverlo.",
                    "Antonio lo intentó y no pudo desplazarlo un milímetro. Aquello debía pesar más de una tonelada.",
                    "Sacó entonces su brújula y miró hacia donde apuntaba la aguja.",
                    "A cuarenta o cincuenta metros había varios afloramientos rocosos, como grandes bochas de granito.",
                    "Miraron los dos en la dirección Norte, poniendo la brújula sobre el tronco petrificado para que quedara quieta, y sólo dos rocas quedaban en línea.",
                    "Debíamos haber traído con qué medir – dijo Antonio.",
                    "No importa, lo medimos con pasos.",
                    "¿Vos sabés cuánto mide tu paso?",
                    "No, pero sé que es menos de un metro, porque una vez mi padre y yo medimos una chacra.",
                    "Bueno, vamos juntos. Vos contá tus pasos y yo los míos.",
                    "Cuando llegaron a la primera bocha, Luis dijo:",
                    "Treinta y ocho.",
                    "Treinta y nueve – anunció Antonio.",
                    "Era pues, la segunda roca. Siguieron hasta ella y Luis contó cincuenta y tres pasos.",
                    "Tenía que ser allí. Empuñó el pico y marcó a golpes el perímetro de lo que iban a escarbar, del mismo ancho que la piedra.",
                    "Tomó la pala de Antonio y, metiéndola en ángulo y luego bajándola hasta dejarla casi paralela al suelo, consiguió sacar entero el pan de césped que había recortado.",
                    "Le pasó la pala a Antonio y le dijo que fuera apilando la tierra en un solo lado.",
                    "Antonio empezó a escarbar y, cuando la profundidad era del largo de la hoja de la pala, golpeó algo duro.",
                    "Dejó la pala, se agacharon y empezaron a sacar a mano la tierra suelta.",
                    "Hay un ladrillo – dijo Luis, y rectificó en seguida –. No, son dos ladrillos.",
                    "Evidentemente estos habían sido puestos por el inglés para proteger la botella, porque cuando consiguieron levantarlos, la encontraron.",
                    "Era una botella verde y grande. Limpiaron primero el pico y vieron que estaba bien tapada, y sellada con lacre.",
                    "Le sacaron la tierra que tenía adherida y vieron que en su interior había unas hojas de papel enrolladas.",
                    "El rollo se había expandido y no iban a poder sacarlas por el pico. Había que romperla.",
                    "Manuscrito encontrado en una botella – dijo Antonio. Yo leí un cuento con ese título, es un libro que me compró papá. No me acuerdo del autor, pero creo que era un inglés o algo parecido.",
                    "Después de mirarla bien, resolvieron llevarla como estaba a las casas y romperla allá.",
                    "Antes, pusieron otra vez los ladrillos y toda la tierra en el pozo, limpiando lo mejor que pudieron y, finalmente, volvieron a colocar el pan de pasto en su lugar, apisonándolo bien.",
                    "En cuanto lloviera, aquello quedaría como antes.",
                    "¡Listo! – dijo Antonio.",
                    "Bueno – dijo Luis –, aunque alguien lo encontrara ahora, no sabría lo que había adentro.",
                    "Tampoco lo sabemos nosotros, todavía. Vámonos de una vez.",
                    "Aunque tenían ganas de salir a matacaballo, tuvieron la fuerza de voluntad y el cariño por sus cabalgaduras como para marchar a aquel trote rendidor de dos leguas por hora.",
                    "Volvieron a las casas, desensillaron, lavaron el lomo a los caballos, los soltaron, y se fueron corriendo al basurero a quebrar la botella.",
                    "Les dio lástima romperla, pero no había otro modo.",
                    "Con el rollo de papel en la mano, corrieron al galpón y lo abrieron.",
                    "Era una carta de John Baker, y decía:",
                    "A quien la encuentre.",
                    "Querido amigo:",
                    "Si estás leyendo esto, quiero creer que no es fruto de la casualidad sino de tu empeño y de lo agudizado de tu mente para descifrar la clave que dejé en la Biblia de los Baker.",
                    "Tuve que ponerla en inglés para que no desentonara y resultara obvia, cuando todas las anotaciones que contiene están escritas en esa lengua.",
                    "Me llamo John Baker, nací en Montevideo en 1847 de padre inglés y madre uruguaya.",
                    "Por ser rubio y de ojos azules, en la zona me llaman El Inglés, como antes le decían a mi padre, que murió hace diez años, en 1887.",
                    "Me crié en este paraje y en él he vivido toda mi vida, salvo tres años que estudié en Montevideo.",
                    "Fui a la escuela en el pequeño poblado cercano de Cañada Seca, a una escuela que mi padre mandó construir y para lo que trajo una maestra.",
                    "Haciendo posible que estudiaran los niños de la región, entre ellos yo.",
                    "Cañada Seca se empezó a crear justamente en torno a la escuela, allá por 1853, cuando mi padre construía el casco de la estancia e hizo surgir la necesidad de comercios, almacenes, policía y otros servicios.",
                    "Me casé en 1874 con Rosaura Gómez, hija de la maestra que había sido mi maestra y que continuaba enseñando en la escuela del pueblo.",
                    "No tuvimos hijos y tuve la desgracia de perderla muy joven, en 1888, al año siguiente de la muerte de mi padre.",
                    "Viudo y solo he vivido los últimos nueve años, pero no soy ni un solitario ni un triste.",
                    "Me gusta la gente, tengo muchos amigos y me considero ducho en muchas cosas, tanto en lides de trabajo como en una partida de taba o truquiflor.",
                    "Escribo versos y a veces los canto con mi guitarra, o en la cercana pulpería me trenzo en una payada de contrapunto si aparece un contendiente.",
                    "Precisamente por espíritu de competencia he dejado mis claves – las que hallaste y las que deberás encontrar – en una suerte de desafío a un innominado contrincante: tú, ignoto amigo.",
                    "Estoy seguro de que serás un muchacho y no un hombre mayor. Sólo los jóvenes tienen fantasía.",
                    "Me gusta la gente inteligente, y deberías serlo para desentrañar el significado de mis claves en dos lenguas.",
                    "Pero el premio lo merece.",
                    "Siempre se dijo en la zona de Cañada Seca que mi padre tenía oro, y algunos intentos de asalto a la estancia lo llevaron a convertirla en una fortaleza.",
                    "Es muy común en las estancias que se guarden monedas de oro, a menudo enterradas en una olla de hierro, y supongo que eso es lo que piensan los que hablan del oro de la estancia.",
                    "Cuando leas el documento que dejó mi padre verás que es otra cosa, mucho más.",
                    "Pero tendrás que encontrarlo.",
                    "Junto con esta carta hallarás una clave para procurar el documento en el que mi padre cuenta su historia.",
                    "Lo encontré entre sus papeles cuando murió, en un sobre dirigido a mí.",
                    "Me imagino que disfrutó escribiéndolo, como disfrutó viviéndolo."
                ]
            },
            {
                'nombre': 'Capítulo 11: El manuscrito de Richard Baker',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Los muchachos terminaron de leer la carta de John Baker.",
                    "¿Qué dice la nueva pista? – preguntó Antonio.",
                    "Luis desplegó el papel que venía junto con la carta.",
                    "Era otro poema, pero esta vez en español:",
                    "En la noche más larga del año,",
                    "Cuando el sol se oculta temprano,",
                    "Busca en el lugar donde el viento",
                    "Susurra secretos al oído.",
                    "¿Qué significa esto? – se preguntó Antonio.",
                    "La noche más larga del año es el solsticio de invierno – dijo Luis.",
                    "Que es el 21 de junio en el hemisferio sur.",
                    "Pero eso es en invierno, y ahora estamos en verano.",
                    "Tendremos que esperar hasta junio para seguir la pista.",
                    "¿Y mientras tanto qué hacemos?",
                    "Guardamos la carta y esperamos. El tesoro no se va a ir.",
                    "Pero tenemos que tener cuidado con el hombre de la cicatriz.",
                    "Que parece estar siguiendo nuestros pasos.",
                    "Los días siguientes pasaron rápidamente.",
                    "Antonio y Luis guardaron la carta de John Baker en un lugar seguro.",
                    "No le contaron a nadie lo que habían encontrado.",
                    "El secreto del tesoro era solo de ellos.",
                    "Terminaron las clases y regresaron a Montevideo.",
                    "Prometieron volver en junio para seguir la pista del solsticio.",
                    "Mientras tanto, estudiaron todo lo que pudieron sobre astronomía.",
                    "Y sobre la historia de Cañada Seca y los Baker.",
                    "El tiempo pasó lentamente, pero finalmente llegó junio.",
                    "Y con él, la noche más larga del año.",
                    "¿Estás listo para la aventura? – preguntó Antonio.",
                    "Más que nunca – respondió Luis.",
                    "El tesoro de Cañada Seca nos espera.",
                    "Pero primero tenemos que descifrar la nueva pista.",
                    "Y evitar al hombre de la cicatriz.",
                    "Que sigue acechando en las sombras."
                ]
            },
            {
                'nombre': 'Capítulo 12: El solsticio de invierno',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "El 21 de junio llegó finalmente.",
                    "Antonio y Luis estaban de vuelta en Cañada Seca.",
                    "La noche más larga del año había comenzado.",
                    "Según la pista, tenían que buscar en el lugar donde el viento susurra secretos.",
                    "¿Dónde puede ser eso? – se preguntó Antonio.",
                    "Luis pensó un momento.",
                    "En la tapera del inglés – dijo –. Allí siempre hay viento.",
                    "Y además, es el lugar más misterioso de toda la zona.",
                    "Tienes razón – dijo Antonio.",
                    "Vamos a la tapera esta noche.",
                    "Pero tenemos que tener cuidado.",
                    "El hombre de la cicatriz puede estar esperándonos.",
                    "Llevemos linternas y estemos atentos.",
                    "El tesoro está cerca, lo siento.",
                    "John Baker nos ha llevado hasta aquí.",
                    "Ahora solo falta el último paso.",
                    "Para encontrar el verdadero tesoro de Cañada Seca.",
                    "En la oscuridad de la noche más larga del año.",
                    "Antonio y Luis llegaron a la tapera del inglés.",
                    "El viento susurraba entre las ruinas.",
                    "Como si les estuviera contando secretos.",
                    "Siguiendo las instrucciones de John Baker.",
                    "Buscaron en el lugar donde el viento era más fuerte.",
                    "Y encontraron una nueva pista escondida.",
                    "Que los llevó al verdadero tesoro.",
                    "No era oro ni joyas.",
                    "Era algo mucho más valioso.",
                    "El manuscrito de Richard Baker.",
                    "Con toda la historia de la familia.",
                    "Y los secretos de Cañada Seca.",
                    "El tesoro era el conocimiento.",
                    "La historia de un lugar y su gente.",
                    "De un inglés que se convirtió en uruguayo.",
                    "Y de dos amigos que descubrieron un misterio.",
                    "Que los unió para siempre.",
                    "El tesoro de Cañada Seca era la amistad."
                ]
            },
            {
                'nombre': 'Capítulo 13: El panteón de los Baker',
                'fondo': 'tapera',
                'personajes': ['antonio', 'luis', 'padre', 'madre'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400), 'padre': (400, 300), 'madre': (400, 350)},
                'textos': [
                    "Pero el manuscrito de Richard Baker contenía una pista más.",
                    "Una pista que los llevaría al verdadero tesoro material.",
                    "En las páginas finales del manuscrito, Richard Baker describía un panteón familiar.",
                    "Un panteón construido en las tierras de la estancia, donde descansaban los restos de la familia.",
                    "Y en ese panteón, según el manuscrito, había algo más que huesos.",
                    "Los muchachos decidieron investigar.",
                    "Con la ayuda de los padres de Luis, localizaron el panteón.",
                    "Era una construcción de piedra, semienterrada en el campo.",
                    "¿Qué buscamos aquí? – preguntó el padre de Luis.",
                    "Según el manuscrito, aquí puede estar el verdadero tesoro – dijo Antonio.",
                    "Los padres se mostraron escépticos, pero accedieron a ayudarlos.",
                    "Con herramientas y linternas, comenzaron a explorar el panteón.",
                    "El piso estaba cubierto de tierra y escombros.",
                    "Pero en una esquina, encontraron algo diferente.",
                    "Una losa que parecía haber sido movida recientemente.",
                    "¿Qué es esto? – preguntó Luis.",
                    "Los muchachos y los padres se pusieron a trabajar.",
                    "Con palas y picos, removieron la tierra alrededor de la losa.",
                    "Y finalmente, lograron levantarla.",
                    "Lo que encontraron los dejó sin aliento.",
                    "Dos arcones de hierro, reforzados con abulonado.",
                    "¡Es el tesoro! – exclamó Antonio.",
                    "Los arcones estaban cerrados con candados antiguos.",
                    "Pero con las herramientas que habían traído, lograron abrirlos.",
                    "Dentro encontraron monedas de oro, documentos antiguos.",
                    "Y reliquias de la familia Baker.",
                    "¡Es increíble! – dijo Luis.",
                    "El tesoro era real, después de todo.",
                    "No solo la amistad y el conocimiento.",
                    "Sino también el oro que tanto se había buscado.",
                    "Los padres de Luis se mostraron asombrados.",
                    "Nunca pensé que encontraríamos algo así – dijo el padre.",
                    "Es como si John Baker hubiera planeado todo esto.",
                    "Para que dos jóvenes como ustedes lo descubrieran.",
                    "El tesoro de Cañada Seca era real.",
                    "Y Antonio y Luis lo habían encontrado.",
                    "Juntos, como amigos.",
                    "Como John Baker había querido.",
                    "Los peones retiraron los picos, él hizo palanca, aumentando la abertura y ellos los metieron, asegurándola.",
                    "Ya había lugar para los dedos y los dos peones y los dos padres consiguieron levantar la lápida, dándola vuelta seguramente hasta apoyarla, invertida, al costado.",
                    "Las cuatro cabezas miraron dentro del panteón, con Antonio y Luis empujando para meter las suyas.",
                    "Un hálito de tiempo encerrado llegó hasta ellos.",
                    "Dentro del panteón había dos estantes de cada lado.",
                    "En cada uno de los estantes superiores, había un viejo ataúd.",
                    "Los otros dos estantes estaban vacíos.",
                    "El padre de Luis trajo la escalera y la introdujo por la abertura, haciéndola llegar hasta abajo.",
                    "Uno de los peones bajó hasta la altura de los cajones.",
                    "-Richard Baker y Rosaura, la mujer de John – susurró Luis.",
                    "Las tablas de los cajones estaban sueltas y podridas.",
                    "El peón levantó la tapa de uno y luego del otro, dejándolas resbalar hacia atrás.",
                    "Lo único que contenía cada cajón era un esqueleto.",
                    "-No hay nada – dijo el peón.",
                    "El padre de Antonio se acercó a mirar y llamó al de Luis.",
                    "-Mirá – le dijo -, eso no es simétrico. ¿Por qué?",
                    "El padre de Luis se asomó y vio que, mientras a la izquierda, debajo del estante inferior había lugar de sobra para poner otro cajón, a la derecha ese espacio estaba cerrado por una pared que, desde el borde del estante, bajaba hasta el piso.",
                    "Con ademán urgente tomó un pico, se lo alcanzó al peón que seguía adentro y le dijo:",
                    "-Rompe esa pared.",
                    "Con cierta dificultad por la falta de espacio, empezó a picar la pared hasta que un ladrillo cayó hacia adentro.",
                    "Metió la mano por el agujero y gritó hacia arriba:",
                    "-¡Es hueco!",
                    "Siguió agrandando el agujero y, cuando el tamaño permitía pasar la cabeza, el padre de Luis le gritó:",
                    "-¡Pará! – y bajó con una linterna.",
                    "-Subí – le dijo al peón.",
                    "Prendió la linterna y metió juntos el brazo y la cabeza por el agujero.",
                    "Se oyó una exclamación y los de arriba lo vieron incorporarse, tomar el pico y, como loco, empezar a hacer volar pedazos de la pared.",
                    "Los de arriba se desgañitaban preguntándose qué había visto, pero él parecía no oírlos, déle y déle golpe.",
                    "Cuando el agujero llegó hasta el piso, soltó la herramienta, tomó algo que estaba adentro y empezó a hacer fuerza con las dos manos, hasta quedar violeta.",
                    "-¡Pesa una tonelada! – se le oyó exclamar y, acto seguido, subió como una tromba por la escalera, saltó del panteón al suelo y ya iba a seguir corriendo cuando el padre de Antonio lo tomó del brazo:",
                    "-¿Qué hay? ¿Encontraste algo?",
                    "-¡Hay dos arcones reforzados con hierro abulonado, que no los mueve nadie! ¡Voy a buscar un guinche o un aparejo!"
                ]
            },
            {
                'nombre': 'Capítulo 14: El legado de John Baker',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Los días siguientes fueron de gran actividad.",
                    "Los arcones fueron trasladados a las casas de Luis.",
                    "Y allí, con cuidado, fueron inventariando su contenido.",
                    "Monedas de oro de diferentes épocas.",
                    "Documentos históricos de gran valor.",
                    "Cartas y diarios de la familia Baker.",
                    "Y el manuscrito completo de Richard Baker.",
                    "Todo estaba perfectamente conservado.",
                    "Como si John Baker hubiera querido preservar la historia.",
                    "Para que futuras generaciones la conocieran.",
                    "¿Qué hacemos con todo esto? – preguntó Luis.",
                    "Antonio pensó un momento.",
                    "Creo que deberíamos donar los documentos a un museo.",
                    "Para que todos puedan conocer la historia.",
                    "Y las monedas...",
                    "Las monedas podrían ayudar a tu familia.",
                    "A mejorar la estancia, a comprar más tierras.",
                    "Luis asintió.",
                    "Tienes razón. Es lo que John Baker hubiera querido.",
                    "Que su tesoro sirviera para algo bueno.",
                    "Para mantener viva la historia de Cañada Seca.",
                    "Y para ayudar a las familias que viven aquí.",
                    "Los muchachos se sintieron orgullosos.",
                    "Habían resuelto el misterio del tesoro.",
                    "Y habían encontrado algo más valioso que el oro.",
                    "La amistad verdadera.",
                    "Y el conocimiento de que juntos pueden lograr cualquier cosa.",
                    "El tesoro de Cañada Seca había sido encontrado.",
                    "No solo el oro y los documentos.",
                    "Sino también la amistad entre Antonio y Luis.",
                    "Una amistad que duraría toda la vida.",
                    "Como el legado de John Baker.",
                    "Que perduraría en la memoria de Cañada Seca.",
                    "Para siempre."
                ]
            },
            {
                'nombre': 'Capítulo 15: El regreso a Montevideo',
                'fondo': 'colegio',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Las vacaciones terminaron y los muchachos regresaron a Montevideo.",
                    "Pero esta vez no volvieron solos.",
                    "Llevaban con ellos la experiencia de una gran aventura.",
                    "Y la certeza de que habían encontrado algo extraordinario.",
                    "En el colegio, sus amigos los esperaban ansiosos.",
                    "¿Qué pasó? ¿Encontraron algo?",
                    "Antonio y Luis se miraron y sonrieron.",
                    "Sí, encontramos mucho más de lo que esperábamos.",
                    "¿El tesoro era real?",
                    "Más real de lo que pensábamos.",
                    "Los muchachos contaron su historia.",
                    "De la tapera del inglés, de las luces malas.",
                    "De la curandera y la Biblia antigua.",
                    "De la botella enterrada y la carta de John Baker.",
                    "De la excavación y el hallazgo del panteón.",
                    "Y finalmente, de los arcones de hierro.",
                    "Sus amigos escucharon fascinados.",
                    "Es como una novela de aventuras – dijo uno.",
                    "Pero es real – respondió Luis.",
                    "Todo es real.",
                    "Y lo más importante es que lo hicimos juntos.",
                    "Antonio y Luis habían cambiado.",
                    "No solo por la aventura que habían vivido.",
                    "Sino por la amistad que habían fortalecido.",
                    "Una amistad que los había llevado a descubrir.",
                    "No solo el tesoro de Cañada Seca.",
                    "Sino también el valor de la amistad verdadera.",
                    "Y el poder de trabajar juntos.",
                    "Para lograr algo extraordinario.",
                    "El tesoro de Cañada Seca era real.",
                    "Y ellos lo habían encontrado.",
                    "Juntos."
                ]
            },
            {
                'nombre': 'Capítulo 16: El futuro',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Los años pasaron y Antonio y Luis crecieron.",
                    "Pero su amistad nunca se debilitó.",
                    "Cada verano, Antonio volvía a Cañada Seca.",
                    "Y juntos recordaban su gran aventura.",
                    "El tesoro había cambiado sus vidas.",
                    "Las monedas de oro habían ayudado a la familia de Luis.",
                    "A mejorar la estancia y comprar más tierras.",
                    "Los documentos habían sido donados a un museo.",
                    "Donde ahora todos pueden conocer la historia.",
                    "De Richard Baker y su hijo John.",
                    "Y del tesoro de Cañada Seca.",
                    "Pero el verdadero tesoro era su amistad.",
                    "Una amistad que había nacido en el colegio.",
                    "Y que se había fortalecido en la aventura.",
                    "Antonio y Luis sabían que siempre serían amigos.",
                    "Como John Baker había querido.",
                    "Que su tesoro uniera a dos jóvenes.",
                    "En una amistad que duraría toda la vida.",
                    "El tesoro de Cañada Seca era real.",
                    "Y ellos lo habían encontrado.",
                    "Juntos.",
                    "Para siempre."
                ]
            },
            {
                'nombre': 'Capítulo 17: Epílogo',
                'fondo': 'tapera',
                'personajes': [],
                'posiciones': {},
                'textos': [
                    "En la tapera del inglés, el viento sigue susurrando.",
                    "Como si contara la historia a quien quiera escuchar.",
                    "La historia de Richard Baker y su hijo John.",
                    "De dos jóvenes que encontraron un tesoro.",
                    "Y de una amistad que duró toda la vida.",
                    "El tesoro de Cañada Seca era real.",
                    "No solo el oro y los documentos.",
                    "Sino también la amistad verdadera.",
                    "Y el conocimiento de que juntos se puede lograr cualquier cosa.",
                    "John Baker había planeado todo perfectamente.",
                    "Para que dos jóvenes como Antonio y Luis.",
                    "Descubrieran no solo su tesoro material.",
                    "Sino también el valor de la amistad.",
                    "Y el poder de trabajar juntos.",
                    "Para lograr algo extraordinario.",
                    "El tesoro de Cañada Seca había sido encontrado.",
                    "Y su historia perduraría para siempre.",
                    "En la memoria de todos los que la conocieran.",
                    "Como una leyenda que se convirtió en realidad.",
                    "Gracias a la amistad de dos jóvenes.",
                    "Que se atrevieron a soñar.",
                    "Y a buscar el tesoro de Cañada Seca.",
                    "Juntos."
                ]
            },
            {
                'nombre': 'Capítulo 18: El legado continúa',
                'fondo': 'campo',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "Muchos años después, Antonio y Luis seguían siendo amigos.",
                    "Sus hijos crecieron escuchando la historia.",
                    "Del tesoro de Cañada Seca.",
                    "Y de cómo dos jóvenes lo encontraron.",
                    "La estancia de Luis había prosperado.",
                    "Gracias al tesoro que habían encontrado.",
                    "Y la historia se había convertido en leyenda.",
                    "En Cañada Seca, todos conocían la historia.",
                    "De Richard Baker y su hijo John.",
                    "Y de los dos jóvenes que encontraron el tesoro.",
                    "El panteón de los Baker se había convertido en un lugar de peregrinación.",
                    "Donde la gente iba a recordar la historia.",
                    "Y a soñar con encontrar su propio tesoro.",
                    "Pero el verdadero tesoro ya había sido encontrado.",
                    "La amistad entre Antonio y Luis.",
                    "Que había durado toda la vida.",
                    "Y que seguiría durando.",
                    "En la memoria de sus hijos y nietos.",
                    "Como el legado de John Baker.",
                    "Que había querido que su tesoro uniera a dos jóvenes.",
                    "En una amistad que duraría para siempre.",
                    "El tesoro de Cañada Seca era real.",
                    "Y su historia nunca se olvidaría.",
                    "Porque era una historia de amistad.",
                    "De aventura y de sueños.",
                    "Que se hicieron realidad.",
                    "Gracias a dos jóvenes valientes.",
                    "Que se atrevieron a buscar.",
                    "El tesoro de Cañada Seca.",
                    "Juntos."
                ]
            },
            {
                'nombre': 'Capítulo 19: La nueva generación',
                'fondo': 'colegio',
                'personajes': [],
                'posiciones': {},
                'textos': [
                    "En el colegio de Montevideo, una nueva generación de estudiantes.",
                    "Escuchaba la historia del tesoro de Cañada Seca.",
                    "Contada por Antonio y Luis, ahora adultos.",
                    "Que habían vuelto a visitar su antiguo colegio.",
                    "Para compartir su historia con los jóvenes.",
                    "Y enseñarles el valor de la amistad.",
                    "Y el poder de soñar.",
                    "Los estudiantes escuchaban fascinados.",
                    "Como si fuera una novela de aventuras.",
                    "Pero sabían que era real.",
                    "Porque Antonio y Luis estaban allí.",
                    "Contándoles su historia.",
                    "De cómo encontraron el tesoro.",
                    "Y de cómo su amistad duró toda la vida.",
                    "Los jóvenes se preguntaban.",
                    "Si ellos también podrían tener una aventura así.",
                    "Y encontrar su propio tesoro.",
                    "Antonio y Luis les decían que sí.",
                    "Que todos tienen su propio tesoro que encontrar.",
                    "No necesariamente de oro.",
                    "Sino de amistad, de conocimiento, de sueños.",
                    "Y que la clave está en buscar juntos.",
                    "Como ellos lo habían hecho.",
                    "El tesoro de Cañada Seca había inspirado.",
                    "A una nueva generación de soñadores.",
                    "Que se atreverían a buscar sus propios tesoros.",
                    "Y a formar amistades que durarían toda la vida.",
                    "Como la de Antonio y Luis.",
                    "Que había comenzado en ese mismo colegio.",
                    "Muchos años antes.",
                    "Cuando dos jóvenes se atrevieron a soñar.",
                    "Y a buscar el tesoro de Cañada Seca.",
                    "Juntos."
                ]
            },
            {
                'nombre': 'Capítulo 20: El tesoro verdadero',
                'fondo': 'tapera',
                'personajes': ['antonio', 'luis'],
                'posiciones': {'antonio': (100, 400), 'luis': (700, 400)},
                'textos': [
                    "En la tapera del inglés, Antonio y Luis se encontraron una última vez.",
                    "Ya ancianos, pero con la misma amistad de siempre.",
                    "El viento susurraba entre las ruinas.",
                    "Como si les recordara su gran aventura.",
                    "¿Te acuerdas cuando encontramos el tesoro? – preguntó Antonio.",
                    "Como si fuera ayer – respondió Luis.",
                    "Pero el verdadero tesoro no era el oro.",
                    "Era nuestra amistad.",
                    "Que ha durado toda la vida.",
                    "Y que durará para siempre.",
                    "En la memoria de nuestros hijos y nietos.",
                    "Y en la historia de Cañada Seca.",
                    "John Baker había planeado todo perfectamente.",
                    "Para que su tesoro uniera a dos jóvenes.",
                    "En una amistad que duraría toda la vida.",
                    "Y que inspiraría a generaciones futuras.",
                    "A buscar sus propios tesoros.",
                    "Y a formar amistades verdaderas.",
                    "El tesoro de Cañada Seca era real.",
                    "No solo el oro y los documentos.",
                    "Sino también la amistad entre Antonio y Luis.",
                    "Que había durado toda la vida.",
                    "Y que seguiría durando.",
                    "En la memoria de todos los que conocieran su historia.",
                    "Como una leyenda que se convirtió en realidad.",
                    "Gracias a dos jóvenes valientes.",
                    "Que se atrevieron a soñar.",
                    "Y a buscar el tesoro de Cañada Seca.",
                    "Juntos.",
                    "Para siempre.",
                    "El tesoro de Cañada Seca había sido encontrado.",
                    "Y su historia nunca se olvidaría.",
                    "Porque era una historia de amistad.",
                    "De aventura y de sueños.",
                    "Que se hicieron realidad.",
                    "Gracias a la amistad de dos jóvenes.",
                    "Que se atrevieron a buscar.",
                    "El tesoro de Cañada Seca.",
                    "Juntos.",
                    "Para siempre."
                ]
            }
        ]
        
        self.capitulo_actual = 0
        self.linea_actual = 0
        self.estado = 'menu'  # 'menu', 'historia', 'seleccion_capitulo', 'pausa'
        
        # Elementos del menú
        self.boton_rect = pygame.Rect(300, 400, 200, 60)
        self.fuente_boton = pygame.font.SysFont('arial', 36)
        self.color_boton = (70, 130, 180)
        self.color_boton_hover = (100, 160, 210)
        self.boton_hover = False
        
        # Botones de navegación
        self.boton_anterior = pygame.Rect(50, 500, 150, 40)
        self.boton_siguiente = pygame.Rect(600, 500, 150, 40)
        self.boton_anterior_hover = False
        self.boton_siguiente_hover = False
        
        # Botón de pausa (esquina superior derecha)
        self.boton_pausa = pygame.Rect(720, 20, 60, 40)
        self.boton_pausa_hover = False
        
        # Botones del menú de pausa
        self.boton_reanudar = pygame.Rect(300, 250, 200, 60)
        self.boton_salir = pygame.Rect(300, 350, 200, 60)
        self.boton_reanudar_hover = False
        self.boton_salir_hover = False
        
        self.caja_texto_rect = pygame.Rect(40, 450, 720, 120)

    def evento(self, event):
        if self.estado == 'menu':
            if event.type == pygame.MOUSEMOTION:
                self.boton_hover = self.boton_rect.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.boton_rect.collidepoint(event.pos):
                    self.estado = 'seleccion_capitulo'
                    
        elif self.estado == 'seleccion_capitulo':
            if event.type == pygame.MOUSEMOTION:
                self.boton_anterior_hover = self.boton_anterior.collidepoint(event.pos)
                self.boton_siguiente_hover = self.boton_siguiente.collidepoint(event.pos)
                self.boton_pausa_hover = self.boton_pausa.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.boton_anterior.collidepoint(event.pos):
                    self.capitulo_actual = max(0, self.capitulo_actual - 1)
                elif self.boton_siguiente.collidepoint(event.pos):
                    self.capitulo_actual = min(len(self.escenas) - 1, self.capitulo_actual + 1)
                elif self.boton_rect.collidepoint(event.pos):
                    self.estado = 'historia'
                    self.linea_actual = 0
                elif self.boton_pausa.collidepoint(event.pos):
                    self.estado_anterior = self.estado
                    self.estado = 'pausa'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.estado = 'menu'
                    
        elif self.estado == 'historia':
            if event.type == pygame.MOUSEMOTION:
                self.boton_pausa_hover = self.boton_pausa.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.boton_pausa.collidepoint(event.pos):
                    self.estado_anterior = self.estado
                    self.estado = 'pausa'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.linea_actual += 1
                    if self.linea_actual >= len(self.escenas[self.capitulo_actual]['textos']):
                        self.linea_actual = len(self.escenas[self.capitulo_actual]['textos']) - 1
                elif event.key == pygame.K_ESCAPE:
                    self.estado = 'seleccion_capitulo'
                    
        elif self.estado == 'pausa':
            if event.type == pygame.MOUSEMOTION:
                self.boton_reanudar_hover = self.boton_reanudar.collidepoint(event.pos)
                self.boton_salir_hover = self.boton_salir.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.boton_reanudar.collidepoint(event.pos):
                    # Volver al estado anterior
                    if hasattr(self, 'estado_anterior'):
                        self.estado = self.estado_anterior
                    else:
                        self.estado = 'seleccion_capitulo'
                elif self.boton_salir.collidepoint(event.pos):
                    self.estado = 'menu'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Volver al estado anterior
                    if hasattr(self, 'estado_anterior'):
                        self.estado = self.estado_anterior
                    else:
                        self.estado = 'seleccion_capitulo'

    def actualizar(self):
        pass

    def dibujar(self):
        if self.estado == 'menu':
            fondo_escalado = pygame.transform.scale(self.fondos['colegio'], (800, 600))
            self.pantalla.blit(fondo_escalado, (0, 0))
            
            # Título del juego
            titulo = self.fuente_boton.render('El Tesoro de Cañada Seca', True, (255, 255, 255))
            titulo_rect = titulo.get_rect(center=(400, 200))
            self.pantalla.blit(titulo, titulo_rect)
            
            # Botón jugar
            color = self.color_boton_hover if self.boton_hover else self.color_boton
            pygame.draw.rect(self.pantalla, color, self.boton_rect)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_rect, 3)
            texto_boton = self.fuente_boton.render('Jugar', True, (255, 255, 255))
            text_rect = texto_boton.get_rect(center=self.boton_rect.center)
            self.pantalla.blit(texto_boton, text_rect)
            
        elif self.estado == 'seleccion_capitulo':
            # Fondo del capítulo actual
            escena_actual = self.escenas[self.capitulo_actual]
            fondo_escalado = pygame.transform.scale(self.fondos[escena_actual['fondo']], (800, 600))
            self.pantalla.blit(fondo_escalado, (0, 0))
            
            # Título del capítulo
            titulo = self.fuente_boton.render(escena_actual['nombre'], True, (255, 255, 255))
            titulo_rect = titulo.get_rect(center=(400, 100))
            self.pantalla.blit(titulo, titulo_rect)
            
            # Personajes de la escena
            for personaje in escena_actual['personajes']:
                pos = escena_actual['posiciones'][personaje]
                self.pantalla.blit(self.personajes[personaje], pos)
            
            # Botones de navegación
            color_anterior = (100, 160, 210) if self.boton_anterior_hover else (70, 130, 180)
            color_siguiente = (100, 160, 210) if self.boton_siguiente_hover else (70, 130, 180)
            
            pygame.draw.rect(self.pantalla, color_anterior, self.boton_anterior)
            pygame.draw.rect(self.pantalla, color_siguiente, self.boton_siguiente)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_anterior, 2)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_siguiente, 2)
            
            texto_anterior = self.fuente.render('Anterior', True, (255, 255, 255))
            texto_siguiente = self.fuente.render('Siguiente', True, (255, 255, 255))
            self.pantalla.blit(texto_anterior, (self.boton_anterior.centerx - 40, self.boton_anterior.centery - 10))
            self.pantalla.blit(texto_siguiente, (self.boton_siguiente.centerx - 40, self.boton_siguiente.centery - 10))
            
            # Botón jugar
            color = self.color_boton_hover if self.boton_hover else self.color_boton
            pygame.draw.rect(self.pantalla, color, self.boton_rect)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_rect, 3)
            texto_boton = self.fuente_boton.render('Jugar Capítulo', True, (255, 255, 255))
            text_rect = texto_boton.get_rect(center=self.boton_rect.center)
            self.pantalla.blit(texto_boton, text_rect)
            
            # Instrucciones
            instruccion = self.fuente.render("Usa los botones para navegar entre capítulos, ESC para volver", True, (255, 255, 255))
            self.pantalla.blit(instruccion, (20, 580))
            
            # Botón de pausa
            color_pausa = (100, 160, 210) if self.boton_pausa_hover else (70, 130, 180)
            pygame.draw.rect(self.pantalla, color_pausa, self.boton_pausa)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_pausa, 2)
            texto_pausa = self.fuente.render("⏸", True, (255, 255, 255))
            self.pantalla.blit(texto_pausa, (self.boton_pausa.centerx - 10, self.boton_pausa.centery - 10))
            
        elif self.estado == 'historia':
            escena_actual = self.escenas[self.capitulo_actual]
            fondo_escalado = pygame.transform.scale(self.fondos[escena_actual['fondo']], (800, 600))
            self.pantalla.blit(fondo_escalado, (0, 0))
            
            # Personajes de la escena
            for personaje in escena_actual['personajes']:
                pos = escena_actual['posiciones'][personaje]
                self.pantalla.blit(self.personajes[personaje], pos)
            
            # Caja de texto
            pygame.draw.rect(self.pantalla, (30, 30, 30), self.caja_texto_rect)
            pygame.draw.rect(self.pantalla, (200, 200, 200), self.caja_texto_rect, 2)
            
            if self.linea_actual < len(escena_actual['textos']):
                texto = escena_actual['textos'][self.linea_actual]
                max_width = self.caja_texto_rect.width - 40
                wrapped_lines = self.wrap_text(texto, self.fuente, max_width)
                y = self.caja_texto_rect.y + 20
                for linea in wrapped_lines:
                    render = self.fuente.render(linea, True, (255, 255, 255))
                    self.pantalla.blit(render, (self.caja_texto_rect.x + 20, y))
                    y += self.fuente.get_height() + 4
            
            # Instrucciones
            instruccion = self.fuente.render("Presiona ESPACIO para continuar, ESC para volver a selección", True, (255, 255, 255))
            self.pantalla.blit(instruccion, (20, 580))
            
            # Botón de pausa
            color_pausa = (100, 160, 210) if self.boton_pausa_hover else (70, 130, 180)
            pygame.draw.rect(self.pantalla, color_pausa, self.boton_pausa)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_pausa, 2)
            texto_pausa = self.fuente.render("⏸", True, (255, 255, 255))
            self.pantalla.blit(texto_pausa, (self.boton_pausa.centerx - 10, self.boton_pausa.centery - 10))
            
        elif self.estado == 'pausa':
            # Fondo semi-transparente
            superficie_oscura = pygame.Surface((800, 600))
            superficie_oscura.set_alpha(128)
            superficie_oscura.fill((0, 0, 0))
            self.pantalla.blit(superficie_oscura, (0, 0))
            
            # Título del menú de pausa
            titulo = self.fuente_boton.render('PAUSA', True, (255, 255, 255))
            titulo_rect = titulo.get_rect(center=(400, 150))
            self.pantalla.blit(titulo, titulo_rect)
            
            # Botón Reanudar
            color_reanudar = (100, 160, 210) if self.boton_reanudar_hover else (70, 130, 180)
            pygame.draw.rect(self.pantalla, color_reanudar, self.boton_reanudar)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_reanudar, 3)
            texto_reanudar = self.fuente_boton.render('Reanudar', True, (255, 255, 255))
            text_rect_reanudar = texto_reanudar.get_rect(center=self.boton_reanudar.center)
            self.pantalla.blit(texto_reanudar, text_rect_reanudar)
            
            # Botón Salir
            color_salir = (100, 160, 210) if self.boton_salir_hover else (70, 130, 180)
            pygame.draw.rect(self.pantalla, color_salir, self.boton_salir)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.boton_salir, 3)
            texto_salir = self.fuente_boton.render('Salir', True, (255, 255, 255))
            text_rect_salir = texto_salir.get_rect(center=self.boton_salir.center)
            self.pantalla.blit(texto_salir, text_rect_salir)
            
            # Instrucciones
            instruccion = self.fuente.render("Presiona ESC para reanudar", True, (255, 255, 255))
            self.pantalla.blit(instruccion, (20, 580))

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + ' '
        if current_line:
            lines.append(current_line.strip())
        return lines 