# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2023 Jim Schmitz
#
#   This library is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 2.1 of the License, or (at
#   your option) any later version.
#
#   This library is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
#   General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************
import string


# many thanks to Peter Norvig for his spelling corrector tutorial:
# http://norvig.com/spell-correct.html


def edits1(word):
    letters = (string.ascii_uppercase if word == word.upper()
               else string.ascii_lowercase) + '_'

    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]

    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def known(words, dictionary):
    return list(set(w for w in words if w in dictionary))


def candidates(word, dictionary):
    if word in dictionary:
        return set([word])
    else:
        return known(
            edits1(word),
            dictionary) or (
            len(word) <= 10 and known(
                edits2(word),
                dictionary)) or []


def suggestions(word, word_list):
    words = ['"' + w + '"' for w in sorted(candidates(word, word_list))]
    if len(words) == 0:
        return None
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return words[0] + ' or ' + words[1]
    else:
        return ', '.join(words[:-1]) + ', or ' + words[-1]


def error_msg(obj_name, word, obj, module=False):
    msg = 'py5 has no field or function' if module else obj_name + \
        ' objects have no fields or methods'
    msg += ' named "' + word + '"'

    if word and word[0] != '_' and (
        suggestion_list := suggestions(
            word, set(
            dir(obj)))):
        msg += '. Did you mean ' + suggestion_list + '?'

    return msg
