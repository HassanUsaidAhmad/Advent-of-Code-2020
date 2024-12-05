package utils

import (
	"strings"
)

func ArrayToString(arr []string) string {
	return strings.Join([]string(arr), " ")
}
