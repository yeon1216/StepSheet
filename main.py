import time
import re
import member
from sheet_util import *
from util import *


def getAllMember():
    worksheet = getSheet(ALL_MEMBER_SHEET)
    range_list = worksheet.range(RANGE)
    member_list = []
    temp_member_id = -1
    temp_member_name = ''
    temp_member_state = -1
    temp_join_date = ''
    temp_age = -1
    for idx, cell in enumerate(range_list):
        if idx % 6 == 0:
            if cell.value == 'end':
                break
            temp_member_id = cell.value
        elif idx % 6 == 1:
            temp_member_name = cell.value
        elif idx % 6 == 2:
            temp_member_state = cell.value
        elif idx % 6 == 3:
            temp_join_date = cell.value
        elif idx % 6 == 4:
            temp_age = cell.value
        else:
            member_list.append(
                member.Member(temp_member_id, temp_member_name, temp_member_state, temp_join_date, temp_age))

    return member_list


def getActivateMemberList():
    worksheet = getSheet(ALL_MEMBER_SHEET)
    range_list = worksheet.range(RANGE)
    activate_member_list = []
    temp_member_id = -1
    temp_member_name = ''
    temp_member_state = -1
    temp_join_date = ''
    temp_age = -1
    for idx, cell in enumerate(range_list):
        if idx % 6 == 0:
            if cell.value == 'end':
                break
            temp_member_id = cell.value
        elif idx % 6 == 1:
            temp_member_name = cell.value
        elif idx % 6 == 2:
            temp_member_state = cell.value
        elif idx % 6 == 3:
            temp_join_date = cell.value
        elif idx % 6 == 4:
            temp_age = cell.value
        else:
            try:
                if int(temp_member_state) == 1 or int(temp_member_state) == 2 or int(temp_member_state) == 3:
                    activate_member_list.append(
                        member.Member(temp_member_id, temp_member_name, temp_member_state, temp_join_date, temp_age))
            except Exception as e:
                break

    return activate_member_list


def member_list_print(list):
    for member in list:
        member.print()


def print_member_count(list):
    print('member count : ' + str(len(list)))


def write_member(sheet_name, member_list):
    worksheet = getSheet(sheet_name)
    worksheet.update_acell('A1', '이름')
    worksheet.update_acell('B1', '가입일자')
    worksheet.update_acell('C1', '이번달 출석 여부')
    worksheet.update_acell('D1', '특이사항')

    temp_row = 2
    for member in member_list:
        if int(member.state) == 1 or int(member.state) == 2 or int(member.state) == 3:
            worksheet.update_acell('A' + str(temp_row), member.name)
            worksheet.update_acell('B' + str(temp_row), member.age)
            worksheet.update_acell('C' + str(temp_row), member.join_date)
            temp_row = temp_row + 1
            if temp_row % 10 == 0:
                print('기다리는중...')
                time.sleep(30)
                print('끝')


# def write_live_member_list(sheet_name, member_list):
#     addSheet(sheet_name, len(member_list), 50)
#     write_member(sheet_name, member_list)


def write_today_member(sheet_name, today_badminton_member):
    print('write_today_member(sheet_name, str)')

    date_match = re.search(r'\d+월 \d+일 [가-힣]+', today_badminton_member)
    place_match = re.search(r'사종체', today_badminton_member)
    progress_match = re.search(r'운동 진행 여부 : ([O|X])', today_badminton_member)
    participants_match = re.search(r'운동인원 : (\d+)명', today_badminton_member)

    if date_match:
        date = date_match.group()
    else:
        date = None

    if place_match:
        place = place_match.group()
    else:
        place = None

    if progress_match:
        progress = progress_match.group(1)
    else:
        progress = None

    if participants_match:
        participants = int(participants_match.group(1))
    else:
        participants = None

    # 이름 리스트 추출
    names = re.findall(r'[가-힣]+', today_badminton_member)[9:]

    # 결과 출력
    print("날짜:", date)
    print("운동 진행 여부:", progress)
    print("장소:", place)
    print("운동 인원:", participants)
    print("이름 리스트:", names)

    row = get_row_value_from_date(date)
    worksheet = getSheet(sheet_name)
    worksheet.update_acell(row + str(3), place)
    if progress == 'O':
        worksheet.update_acell(row + str(2), 1)
    if progress == 'X':
        worksheet.update_acell(row + str(2), 0)
        return

    worksheet = getSheet(MONTH_8_SHEET)
    range_list = worksheet.range('A5:A80')
    member_column_dict = {}
    for idx, cell in enumerate(range_list):
        if cell.value == 'end':
            break
        member_column_dict[cell.value] = idx + 5
    for name in names:
        if name == '남':
            continue
        elif name == '여':
            continue
        else:
            worksheet.update_acell(row + str(member_column_dict[name]), 1)


today_badminton_member = '''
8월 4일 금요일 사종체

운동 진행 여부 : O

운동인원 : 15명

곽기훈 00 남
권세영 00 여
김대웅 94 남
김동연 95 남
김성연 93 남
김예림 00 여
김유빈 98 여
김주혜 97 여
류문현 00 남
신준협 95 남
양승빈 98 남
이진용 96 남
임은진 96 여
정상운 00 남
조영재 00 남
'''

if __name__ == '__main__':
    # activate_member_list = getActivateMemberList()
    # print_member_count(activate_member_list)
    # member_list_print(activate_member_list)
    write_today_member('23년 8월', today_badminton_member)
    # print(get_row_value_from_date('8월 30일 화요일'))
