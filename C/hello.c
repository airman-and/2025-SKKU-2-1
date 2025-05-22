#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

#define LED_PIN "17"  // BCM GPIO 17

void write_file(const char *path, const char *value) {
    int fd = open(path, O_WRONLY);
    if (fd < 0) { perror("open"); exit(1); }
    if (write(fd, value, strlen(value)) < 0) { perror("write"); close(fd); exit(1); }
    close(fd);
}

int main(void) {
    // 1) Pin export
    write_file("/sys/class/gpio/export", LED_PIN);
    // 2) Direction 설정
    char path[64];
    snprintf(path, sizeof(path), "/sys/class/gpio/gpio%s/direction", LED_PIN);
    write_file(path, "out");
    // 3) Value 제어
    snprintf(path, sizeof(path), "/sys/class/gpio/gpio%s/value", LED_PIN);
    while (1) {
        write_file(path, "1");  // LED ON
        sleep(1);
        write_file(path, "0");  // LED OFF
        sleep(1);
    }
    return 0;
}
