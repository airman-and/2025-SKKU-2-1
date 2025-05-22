/**
 * C 언어 종합 예제 파일
 * 이 파일은 C 언어의 주요 기능과 문법을 보여줍니다.
 */

#include <stdio.h>      // 표준 입출력 라이브러리
#include <stdlib.h>     // 메모리 할당, 난수 생성 등을 위한 라이브러리
#include <string.h>     // 문자열 처리 함수를 위한 라이브러리
#include <math.h>       // 수학 함수를 위한 라이브러리
#include <time.h>       // 시간 관련 함수를 위한 라이브러리
#include <stdbool.h>    // boolean 타입 사용을 위한 라이브러리

// 매크로 정의 - 컴파일 시 텍스트가 대체됨
#define PI 3.14159
#define SQUARE(x) ((x) * (x))

// 전역 변수 선언
int globalVariable = 100;

// 열거형 정의
enum Days {
    MONDAY = 1,
    TUESDAY,    // 자동으로 2
    WEDNESDAY,  // 자동으로 3
    THURSDAY,   // 자동으로 4
    FRIDAY,     // 자동으로 5
    SATURDAY,   // 자동으로 6
    SUNDAY      // 자동으로 7
};

// 구조체 정의
struct Person {
    char name[50];
    int age;
    float height;
};

// 공용체 정의 - 같은 메모리 공간을 공유하는 여러 변수
union Data {
    int i;
    float f;
    char str[20];
};

// 함수 원형 선언
void demonstrateVariables();
int add(int a, int b);
void swap(int *a, int *b);
void demonstrateArrays();
void demonstrateStrings();
void demonstratePointers();
void demonstrateStructs();
void demonstrateUnions();
void demonstrateFileIO();
void demonstrateRecursion(int n);
void demonstrateMemoryAllocation();
void demonstratePreprocessor();
void callbackExample(int (*callback)(int, int));
int multiply(int a, int b);
void demonstrateVariadicFunction(const char* format, ...);

// 메인 함수 - 프로그램의 시작점
int main() {
    printf("C 언어 종합 예제 시작\n\n");
    
    // 변수와 데이터 타입
    demonstrateVariables();
    
    // 기본 연산자 사용
    printf("\n--- 연산자 ---\n");
    int x = 10, y = 5;
    printf("산술 연산자: %d + %d = %d\n", x, y, x + y);
    printf("산술 연산자: %d - %d = %d\n", x, y, x - y);
    printf("산술 연산자: %d * %d = %d\n", x, y, x * y);
    printf("산술 연산자: %d / %d = %d\n", x, y, x / y);
    printf("산술 연산자: %d %% %d = %d\n", x, y, x % y); // 나머지 연산
    printf("비교 연산자: %d > %d는 %s\n", x, y, x > y ? "참" : "거짓");
    printf("논리 연산자: (x > 5) && (y < 10)는 %s\n", 
           (x > 5) && (y < 10) ? "참" : "거짓");
    
    // 조건문
    printf("\n--- 조건문 ---\n");
    if (x > y) {
        printf("x는 y보다 큽니다.\n");
    } else if (x == y) {
        printf("x는 y와 같습니다.\n");
    } else {
        printf("x는 y보다 작습니다.\n");
    }
    
    // switch 문
    printf("\n--- Switch 문 ---\n");
    enum Days today = WEDNESDAY;
    switch (today) {
        case MONDAY:
            printf("오늘은 월요일입니다.\n");
            break;
        case TUESDAY:
            printf("오늘은 화요일입니다.\n");
            break;
        case WEDNESDAY:
            printf("오늘은 수요일입니다.\n");
            break;
        default:
            printf("다른 요일입니다.\n");
    }
    
    // 반복문
    printf("\n--- 반복문 ---\n");
    printf("for 반복문: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", i);
    }
    printf("\n");
    
    printf("while 반복문: ");
    int j = 0;
    while (j < 5) {
        printf("%d ", j);
        j++;
    }
    printf("\n");
    
    printf("do-while 반복문: ");
    int k = 0;
    do {
        printf("%d ", k);
        k++;
    } while (k < 5);
    printf("\n");
    
    // 함수 사용
    printf("\n--- 함수 사용 ---\n");
    int result = add(10, 20);
    printf("add(10, 20) = %d\n", result);
    
    // 포인터를 이용한 값 교환
    printf("\n--- 포인터로 값 교환 ---\n");
    int a = 5, b = 10;
    printf("교환 전: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("교환 후: a = %d, b = %d\n", a, b);
    
    // 배열 사용
    demonstrateArrays();
    
    // 문자열 처리
    demonstrateStrings();
    
    // 포인터 심화
    demonstratePointers();
    
    // 구조체 사용
    demonstrateStructs();
    
    // 공용체 사용
    demonstrateUnions();
    
    // 파일 입출력
    demonstrateFileIO();
    
    // 재귀 함수
    printf("\n--- 재귀 함수 ---\n");
    printf("재귀 함수로 5부터 카운트다운: ");
    demonstrateRecursion(5);
    printf("\n");
    
    // 동적 메모리 할당
    demonstrateMemoryAllocation();
    
    // 전처리기 지시자
    demonstratePreprocessor();
    
    // 함수 포인터와 콜백
    printf("\n--- 함수 포인터와 콜백 ---\n");
    callbackExample(multiply);
    
    printf("\nC 언어 종합 예제 종료\n");
    return 0;
}

// 변수와 데이터 타입을 보여주는 함수
void demonstrateVariables() {
    printf("\n--- 변수와 데이터 타입 ---\n");
    
    // 기본 데이터 타입
    char c = 'A';                // 문자 (1바이트)
    int i = 42;                  // 정수 (보통 4바이트)
    short s = 100;               // 짧은 정수 (2바이트)
    long l = 1000000L;           // 긴 정수 (최소 4바이트)
    long long ll = 1000000000LL; // 아주 긴 정수 (8바이트)
    float f = 3.14f;             // 단정밀도 부동소수점 (4바이트)
    double d = 3.14159;          // 배정밀도 부동소수점 (8바이트)
    _Bool bool_val = 1;          // 논리값 (C99) 또는 stdbool.h의 bool
    bool bool_val2 = true;       // stdbool.h 사용 시
    
    // 상수 (const 키워드)
    const int FIXED_VALUE = 100;  // 변경할 수 없는 상수
    
    // 변수 출력
    printf("char: %c (ASCII: %d)\n", c, c);
    printf("int: %d\n", i);
    printf("short: %hd\n", s);
    printf("long: %ld\n", l);
    printf("long long: %lld\n", ll);
    printf("float: %.2f\n", f);
    printf("double: %.5f\n", d);
    printf("bool: %d\n", bool_val);
    printf("bool (stdbool.h): %d\n", bool_val2);
    printf("상수: %d\n", FIXED_VALUE);
    printf("전역 변수: %d\n", globalVariable);
    
    // 형변환
    printf("형변환 예: int를 float로: %f\n", (float)i);
}

// 두 정수를 더하는 함수
int add(int a, int b) {
    return a + b;
}

// 포인터를 사용하여 두 변수의 값을 교환하는 함수
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 배열 사용 예제
void demonstrateArrays() {
    printf("\n--- 배열 ---\n");
    
    // 1차원 배열
    int numbers[5] = {10, 20, 30, 40, 50};
    printf("1차원 배열: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    
    // 2차원 배열
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    printf("2차원 배열:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// 문자열 처리 예제
void demonstrateStrings() {
    printf("\n--- 문자열 ---\n");
    
    // 문자열 선언과 초기화
    char greeting[20] = "Hello, World!";
    printf("문자열: %s\n", greeting);
    
    // 문자열 함수 사용
    printf("문자열 길이: %lu\n", strlen(greeting));
    
    // 문자열 복사
    char copy[20];
    strcpy(copy, greeting);
    printf("복사된 문자열: %s\n", copy);
    
    // 문자열 연결
    strcat(copy, " C is fun!");
    printf("연결된 문자열: %s\n", copy);
    
    // 문자열 비교
    printf("strcmp(greeting, \"Hello\"): %d\n", strcmp(greeting, "Hello"));
}

// 포인터 예제
void demonstratePointers() {
    printf("\n--- 포인터 ---\n");
    
    int value = 42;
    int *ptr = &value;  // value의 주소를 포인터에 저장
    
    printf("value: %d\n", value);
    printf("value의 주소: %p\n", (void*)&value);
    printf("ptr이 가리키는 주소: %p\n", (void*)ptr);
    printf("ptr을 통한 값 접근: %d\n", *ptr);
    
    // 포인터를 통한 값 변경
    *ptr = 100;
    printf("포인터로 변경한 후 value: %d\n", value);
    
    // 이중 포인터
    int **pptr = &ptr;
    printf("이중 포인터를 통한 값 접근: %d\n", **pptr);
    
    // void 포인터 (타입 없는 포인터)
    void *vptr = &value;
    printf("void 포인터가 가리키는 주소: %p\n", vptr);
    // void 포인터는 역참조하기 전에 반드시 형변환 필요
    printf("void 포인터의 역참조: %d\n", *(int*)vptr);
}

// 구조체 예제
void demonstrateStructs() {
    printf("\n--- 구조체 ---\n");
    
    // 구조체 변수 선언 및 초기화
    struct Person person1 = {"홍길동", 30, 175.5};
    
    // 구조체 멤버 접근
    printf("이름: %s\n", person1.name);
    printf("나이: %d\n", person1.age);
    printf("키: %.1f cm\n", person1.height);
    
    // 구조체 포인터
    struct Person *personPtr = &person1;
    printf("포인터로 접근: %s, %d세, %.1f cm\n", 
           personPtr->name, personPtr->age, personPtr->height);
    
    // 구조체 배열
    struct Person people[2] = {
        {"김철수", 25, 180.0},
        {"이영희", 28, 165.5}
    };
    printf("구조체 배열: %s, %s\n", people[0].name, people[1].name);
    
    // typedef로 구조체 별칭 만들기
    typedef struct Person Person;
    Person newPerson = {"박지성", 40, 178.0};
    printf("typedef: %s\n", newPerson.name);
}

// 공용체 예제
void demonstrateUnions() {
    printf("\n--- 공용체 ---\n");
    
    union Data data;
    
    // 정수 값 저장
    data.i = 10;
    printf("data.i: %d\n", data.i);
    
    // 실수 값 저장 (이전 값 덮어씀)
    data.f = 220.5f;
    printf("data.f: %.1f\n", data.f);
    printf("data.i: %d\n", data.i);  // 이제 이상한 값이 출력됨
    
    // 문자열 저장 (이전 값 덮어씀)
    strcpy(data.str, "C Programming");
    printf("data.str: %s\n", data.str);
    printf("data.f: %.1f\n", data.f);  // 이제 이상한 값이 출력됨
}

// 파일 입출력 예제
void demonstrateFileIO() {
    printf("\n--- 파일 입출력 ---\n");
    
    // 파일 쓰기
    FILE *file = fopen("test.txt", "w");
    if (file == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return;
    }
    
    fprintf(file, "C 언어로 파일에 쓰기\n");
    fprintf(file, "줄 번호: %d\n", 1);
    fclose(file);
    
    // 파일 읽기
    char buffer[100];
    file = fopen("test.txt", "r");
    if (file == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return;
    }
    
    printf("파일 내용:\n");
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    
    fclose(file);
}

// 재귀 함수 예제
void demonstrateRecursion(int n) {
    if (n <= 0) {
        return;
    }
    printf("%d ", n);
    demonstrateRecursion(n - 1);  // 자기 자신을 호출
}

// 동적 메모리 할당 예제
void demonstrateMemoryAllocation() {
    printf("\n--- 동적 메모리 할당 ---\n");
    
    // malloc(): 메모리 할당
    int *arr = (int*)malloc(5 * sizeof(int));
    if (arr == NULL) {
        printf("메모리 할당 실패\n");
        return;
    }
    
    // 할당된 메모리 사용
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }
    
    printf("malloc()으로 할당된 배열: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // calloc(): 메모리 할당 및 0으로 초기화
    int *arr2 = (int*)calloc(5, sizeof(int));
    if (arr2 == NULL) {
        printf("메모리 할당 실패\n");
        free(arr);  // 이전에 할당한 메모리 해제
        return;
    }
    
    printf("calloc()으로 할당된 배열: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");
    
    // realloc(): 메모리 크기 조정
    int *arr3 = (int*)realloc(arr, 10 * sizeof(int));
    if (arr3 == NULL) {
        printf("메모리 재할당 실패\n");
        free(arr);   // realloc 실패 시 기존 메모리는 그대로 유지됨
        free(arr2);
        return;
    }
    
    // 추가된 메모리 사용
    for (int i = 5; i < 10; i++) {
        arr3[i] = i * 10;
    }
    
    printf("realloc()으로 재할당된 배열: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr3[i]);
    }
    printf("\n");
    
    // 메모리 해제
    free(arr3);  // arr도 여기서 해제됨 (arr3가 가리키는 메모리와 동일)
    free(arr2);
}

// 전처리기 지시자 사용 예제
void demonstratePreprocessor() {
    printf("\n--- 전처리기 지시자 ---\n");
    
    // #define으로 정의된 상수 사용
    printf("PI 값: %.5f\n", PI);
    
    // 매크로 함수 사용
    int num = 5;
    printf("%d의 제곱: %d\n", num, SQUARE(num));
    
    // 조건부 컴파일
#ifdef DEBUG
    printf("디버그 모드입니다.\n");
#else
    printf("릴리스 모드입니다.\n");
#endif

    // __FILE__, __LINE__, __DATE__, __TIME__ 매크로
    printf("파일: %s\n", __FILE__);
    printf("줄: %d\n", __LINE__);
    printf("컴파일 날짜: %s\n", __DATE__);
    printf("컴파일 시간: %s\n", __TIME__);
}

// 콜백 함수를 사용하는 예제
void callbackExample(int (*callback)(int, int)) {
    int result = callback(5, 7);
    printf("콜백 함수의 결과: %d\n", result);
}

// 곱셈 함수 (콜백으로 사용)
int multiply(int a, int b) {
    return a * b;
}

// 가변 인자 함수 예제 (printf와 같은)
#include <stdarg.h>

void demonstrateVariadicFunction(const char* format, ...) {
    va_list args;
    va_start(args, format);
    
    vprintf(format, args);
    
    va_end(args);
}