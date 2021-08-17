"""
Advent of code 2020 day 04
https://adventofcode.com/2020/day/4
"""
from typing import List

TEST_INPUT="""
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

INVALID_TEST="""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

VALID_TEST="""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

class Passport():

    REQUIRED_FIELD = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

    POSSIBLE_ECL = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]

    def __init__(self, passport: str) -> None:
        pp = ''
        for c in passport:
            if c =="\n":
                pp += ' '
            else:
                pp += c
        field_pairs = pp.split(' ')
        fields = []
        values = []
        for field in field_pairs:
            pair = field.split(":")
            fields.append(pair[0])
            values.append(pair[1])
        self.fields = fields
        self.values = values
        self.valid= self.is_valid_passport()

    def __str__(self) -> str:
        res = ''
        for ind, field in enumerate(self.fields):
            res += f"{field}: {self.values[ind]}\n"
        res += str(self.valid)
        return res

    def is_valid_passport(self) -> bool:
        for field in Passport.REQUIRED_FIELD:
            if field not in self.fields:
                return False

        ind = self.fields.index('byr')
        if not(Passport.check_year(self.values[ind], 1920, 2002)):
            return False
        ind = self.fields.index('iyr')
        if not(Passport.check_year(self.values[ind], 2010, 2020)):
            return False
        ind = self.fields.index('eyr')
        if not(Passport.check_year(self.values[ind], 2020, 2030)):
            return False

        ind = self.fields.index('hgt')
        if not(Passport.check_height(self.values[ind])):
            return False

        ind = self.fields.index('hcl')
        if not(Passport.check_hair_color(self.values[ind])):
            return False

        ind = self.fields.index('ecl')
        if not(Passport.check_eye_color(self.values[ind])):
            return False

        ind = self.fields.index('pid')
        if not(Passport.check_passport_id(self.values[ind])):
            return False

        return True

    def check_year(number: str, min: int, max: int) -> bool:
        try:
            if len(number) != 4:
                return False
            val = int(number)
            if min <= val <= max:
                return True
        except:
            return False

    def check_height(height: str)-> bool:
        try:
            unit = height[-2:]
            val = int(height[:-2])
            if unit == "cm":
                return 150 <= val <= 193
            elif unit == "in":
                return 59 <= val <= 76
            else:
                return False
        except IndexError:
            return False
        except IndexError:
            return False

    def check_hair_color(hcl: str)-> bool:
        
        if len(hcl) != 7 or hcl[0] != '#':
            return False 
        allowed_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        for char in hcl[1:]:
            if char not in allowed_char:
                return False
        return True

    def check_eye_color(ecl: str) -> bool:
        return ecl in Passport.POSSIBLE_ECL

    def check_passport_id(pid: str) -> bool:
        if len(pid) != 9:
            return None
        try:
            int(pid)
            return True
        except ValueError:
            return False
       
assert Passport.check_height("60in")
assert Passport.check_height("190cm")
assert not(Passport.check_height("190in"))
assert not(Passport.check_height("190"))

assert Passport.check_hair_color("#123abc")
assert not(Passport.check_hair_color("#123abz"))
assert not(Passport.check_hair_color("123abc"))


assert Passport.check_eye_color('brn')
assert not(Passport.check_eye_color('wat'))

assert Passport.check_passport_id("000000001") 
assert not(Passport.check_passport_id("0123456789")) 

def read_input(input: str) -> List[Passport]:
    list_passport = input.split("\n\n")
    passports = []
    for passport in list_passport:
        passports.append(Passport(passport))
    return passports


def count_valid_passport(passports: List[Passport]) -> int:
    count = 0
    for passport in passports:
        if passport.valid:
            count += 1
    
    return count 

assert count_valid_passport(read_input(INVALID_TEST)) == 0
assert count_valid_passport(read_input(VALID_TEST)) == 4


if __name__ == "__main__":
    file = open('input_day04.txt', mode='r')
    input = file.read()
    file.close()

    passports = read_input(input)
    print(passports[2])
    print(len(passports))
    count = count_valid_passport(passports)
    print(count)