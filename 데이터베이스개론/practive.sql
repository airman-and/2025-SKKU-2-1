-- 테이블 생성
CREATE TABLE student (
  sid CHAR(9) PRIMARY KEY,
  name VARCHAR(20),
  major VARCHAR(30)
);

-- 데이터 삽입
INSERT INTO student VALUES ('2025001', '김현영', 'AI융합');
INSERT INTO student VALUES ('2025002', '이지은', '생명공학');

-- 데이터 조회
SELECT * FROM student;
