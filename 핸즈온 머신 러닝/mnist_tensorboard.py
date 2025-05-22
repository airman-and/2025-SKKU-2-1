import tensorflow as tf
import datetime
import os
import sys

try:
    # MNIST 데이터셋 로드
    print("MNIST 데이터셋을 로드하는 중...")
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # 로그 디렉토리 설정 (현재 디렉토리에 직접 생성)
    current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = os.path.join("tensorboard_logs", current_time)

    # 만약 log_dir에 같은 이름의 파일이 있으면 삭제
    if os.path.isfile(log_dir):
        os.remove(log_dir)
    os.makedirs(log_dir, exist_ok=True)

    # 모델 정의
    print("모델 생성 중...")
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(28, 28)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # 모델 컴파일
    print("모델 컴파일 중...")
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # 텐서보드 콜백 설정
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=log_dir,
        histogram_freq=1,
        write_graph=True,
        write_images=True,
        update_freq='epoch',
        profile_batch=2
    )

    # 모델 학습
    print("모델 학습 시작...")
    model.fit(
        x_train, y_train,
        epochs=5,
        validation_data=(x_test, y_test),
        callbacks=[tensorboard_callback]
    )

    print("\n학습이 완료되었습니다!")
    print("\n텐서보드를 시작하려면 다음 명령어를 실행하세요:")
    print(f"tensorboard --logdir tensorboard_logs")

except Exception as e:
    print(f"\n오류가 발생했습니다: {str(e)}", file=sys.stderr)
    print("\n문제 해결 방법:")
    print("1. tensorflow가 설치되어 있는지 확인하세요: pip install tensorflow")
    print("2. 충분한 디스크 공간이 있는지 확인하세요")
    print("3. 로그 디렉토리에 쓰기 권한이 있는지 확인하세요")
    sys.exit(1) 