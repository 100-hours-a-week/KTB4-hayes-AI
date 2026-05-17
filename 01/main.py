import json
import os
import readline
from datetime import datetime, timedelta

DB_FILE = "schedules.json"

def load_schedules():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_schedules(schedules):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(schedules, f, ensure_ascii=False, indent=4)

def main():
    while True:
        print("\n=== 개인 비서 CLI 프로그램 ===")
        print("1. 입력")
        print("2. 출력")
        print("3. 삭제")
        print("q. 종료")
        
        menu = input("선택: ").strip()
        
        if menu.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
            
        if menu == '1':
            print("\n--- 새 일정 입력 ---")
            date = input("- 일정 날짜 (예: 26.05.17): ").strip()
            title = input("- 일정 제목: ").strip()
            content = input("- 상세 내용: ").strip()
            due_date = input("- 마감 날짜 (예: 26.05.25): ").strip()
            
            schedules = load_schedules()
            schedules.append({
                "date": date,
                "title": title,
                "content": content,
                "due_date": due_date
            })
            save_schedules(schedules)
            print("-> 일정이 안전하게 저장되었습니다.")
            
        elif menu == '2':
            print("\n--- 출력 조건 선택 ---")
            print("1. 오늘 일정 보기")
            print("2. 내일 일정 보기")
            print("3. 그외 날짜 보기")
            
            sub_menu = input("선택: ").strip()
            
            today_dt = datetime.now()
            today_str = today_dt.strftime("%y.%m.%d")
            tomorrow_str = (today_dt + timedelta(days=1)).strftime("%y.%m.%d")
            
            target_date = ""
            if sub_menu == '1':
                target_date = today_str
            elif sub_menu == '2':
                target_date = tomorrow_str
            elif sub_menu == '3':
                target_date = input("조회할 날짜를 입력하세요 (예: 26.05.25): ").strip()
            else:
                print("잘못된 선택입니다.")
                continue
                
            schedules = load_schedules()
            matched_schedules = [s for s in schedules if s["date"] == target_date]
            
            d_minus_2_date = (today_dt + timedelta(days=2)).strftime("%y.%m.%d")
            urgent_schedules = [s for s in schedules if s["due_date"] == d_minus_2_date]
            
            print(f"\n===== [{target_date}] 조회 결과 =====")
            if matched_schedules:
                for idx, s in enumerate(matched_schedules, 1):
                    print(f"{idx}. [{s['title']}] {s['content']} (마감: {s['due_date']})")
            else:
                print("해당 날짜에 등록된 일정이 없습니다.")
                
            print("\n⚠️ [마감 임박! D-2 일정]")
            if urgent_schedules:
                for s in urgent_schedules:
                    print(f"- 🔥 [{s['title']}] {s['content']} (마감일: {s['due_date']})")
            else:
                print("- 마감이 2일 남은 임박 일정이 없습니다.")
            print("====================================")
            
        elif menu == '3':
            schedules = load_schedules()
            if not schedules:
                print("\n-> 등록된 일정이 없어 삭제할 수 없습니다.")
                continue
                
            print("\n--- 현재 전체 일정 목록 ---")
            for idx, s in enumerate(schedules, 1):
                print(f"{idx}. [{s['date']}] {s['title']} (마감: {s['due_date']})")
                
            del_input = input("\n삭제할 일정의 번호를 입력하세요: ").strip()
            
            # 입력값이 숫자인지, 그리고 존재하는 번호 범위 안인지 검사
            if del_input.isdigit() and 1 <= int(del_input) <= len(schedules):
                removed = schedules.pop(int(del_input) - 1)  # 선택한 인덱스의 아이템 삭제
                save_schedules(schedules)                    # 변경된 리스트 저장
                print(f"-> '{removed['title']}' 일정이 정상적으로 삭제되었습니다.")
            else:
                print("잘못된 번호입니다. 삭제를 취소합니다.")

if __name__ == "__main__":
    main()