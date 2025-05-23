# 마크다운(Markdown) 사용법 가이드

## 1. 제목 (Headers)

```markdown
# 제목 1
## 제목 2
### 제목 3
#### 제목 4
##### 제목 5
###### 제목 6
```

## 2. 강조 (Emphasis)

```markdown
*이탤릭체* 또는 _이탤릭체_
**볼드체** 또는 __볼드체__
~~취소선~~
```

## 3. 목록 (Lists)

### 순서 있는 목록

```markdown
1. 첫 번째
2. 두 번째
3. 세 번째
```

### 순서 없는 목록

```markdown
- 항목 1
- 항목 2
  - 하위 항목 2.1
  - 하위 항목 2.2
```

## 4. 링크와 이미지

```markdown
[링크 텍스트](URL)
![이미지 설명](이미지 URL)
```

## 5. 코드 (Code)

### 인라인 코드

인라인 코드는 백틱(`)으로 감싸서 표현합니다: `코드`를 사용합니다.

### 코드 블록

```python
def hello():
    print("Hello, World!")
```

## 6. 인용 (Blockquotes)

```markdown
> 인용문을 작성합니다.
> > 중첩된 인용문
```

## 7. 표 (Tables)

```markdown
| 제목 1 | 제목 2 |
|--------|--------|
| 내용 1 | 내용 2 |
| 내용 3 | 내용 4 |
```

## 8. 수평선

```markdown
---
***
___
```

## 9. 체크 리스트

```markdown
- [x] 완료된 항목
- [ ] 미완료 항목
```

## 10. 각주

```markdown
각주를 달 텍스트[^1]
[^1]: 각주 내용
```

