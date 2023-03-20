from setup import knights

def art():
# ASCII art for knights, items, and actions

    art = {}

    for knight in knights:
        art[knight.code + 'N'] = [\
'            !                 .                ',
'           .^.              .:;:.              ',
'         __|O|__          .:;;;;;:.            ',
'        (_/`-`\_)           ;;;;;              ',
'        //\_K_/\\\\           ;;;;;            '.replace('K',knight.code),
'        \\\\/   \//           ;:;;;            ',
'         8\_v_/8            : ;;;              ',
'           |||                ;:;              ',
'          <-X->             . :.;              ',
'           |||                . :              ',
'          /_|_\             .   .              ']


        art[knight.code + 'S'] = [\
'            !                 .              ',
'           .^.                  .            ',
'         __|O|__            . ;.             ',
'        (_/`-`\_)            .;              ',
'        //\_K_/\\\\             ;;.          '.replace('K',knight.code),
'        \\\\/   \//           ;.;;           ',
'         8\_v_/8            ;;;;.            ',
'           |||              ;;;;;            ',
'          <-X->           ..;;;;;..          ',
'           |||             \':::::\'         ',
'          /_|_\              \':`            ']


        art[knight.code + 'W'] = [\
'            !                                  ',
'           .^.                                 ',
'         __|O|__                               ',
'        (_/`-`\_)         .                    ',
'        //\_K_/\\\\       .;;............ ..   '.replace('K',knight.code),
'        \\\\/   \//     .;;;;::::::::::::..    ',
'         8\_v_/8       \':;;:::::::::::: . .   ',
'           |||           \':                   ',
'          <-X->                                ',
'           |||                                 ',
'          /_|_\                                ']


        art[knight.code + 'E'] = [\
'            !                                   ',
'           .^.                                  ',
'         __|O|__                                ',
'        (_/`-`\_)                     .         ',
'        //\_K_/\\\\      .. ............;;.     '.replace('K',knight.code),
'        \\\\/   \//      ..::::::::::::;;;;.    ',
'         8\_v_/8     . . ::::::::::::;;:\'      ',
'           |||                        :\'       ',
'          <-X->                                 ',
'           |||                                  ',
'          /_|_\                                 ']


    art['DEAD'] = [\
'                          ',
'           __ _           ',
'         .\'    \'.       ',
'        / _   _  \\       ',
'        )(.) (.)(;        ',
'        {  AA   }.        ',
'         \\uuuuu\'(       ',
'          )     )         ',
'         /nnnnn//         ',
'         \_.-._/          ',
'                          ']


    art['DROWNED'] = [\
'                               ',
'                               ',
'         11        11          ',
'         11J      L11          ',
'         //   !    \\\\        ',
'        <>   .^.   <>          ',
'         \\\\__|O|__//         ',
'          (_/`-`\_)            ',
'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
'                               ',
'                               ']

    art['A'] = [\
'      ,  /\\  .     ',
'     //`-||-\'\\\\  ',
'    (| -=||=- |)    ',
'     \\\\,-||-.//   ',
'      `  ||  \'     ',
'         ||         ',
'         ||         ',
'         ||         ',
'         ||         ',
'         ||         ',
'         ()         ']

    art['D'] = [\
'         .-.       ',
'         |-|       ',
'         |-|       ',
'      :==^~^==:    ',
'      :-------:    ',
'         |||       ',
'         |||       ',
'         |||       ',
'         |\'|      ',
'         \\ /      ',
'          V        ']

    art['M'] = [\
'       *  *  *      ',
'        \\ | /      ',
'         \\|/       ',
'     *--<{O}>--*    ',
'          \\\\      ',
'           \\\\     ',
'           //       ',
'          //        ',
'          \\\\      ',
'          //        ',
'          O         ']

    art['H'] = [\
'                     ',
'         _,.         ',
'       ,` -.)        ',
'      ( _/-\\\\-._   ',
'     /,|`--._.-\'|   ',
'     \\_| |\\___/||  ',
'       |  \\___/ |   ',
'       |    ||  ;    ',
'       `~.  || /     ',
'          `~||/      ',
'                     ']

    return art