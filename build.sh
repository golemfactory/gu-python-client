#! /bin/bash
#

fail() {
	echo $@ >&2
	exit 1
}

test_tool() {
	which "$1" >/dev/null || fail "$2"
}

test_tool openapi-generator "missing openapi-generator, install with: npm install -g openapi-generator"
test_tool patch "missing patch. install with: apt install patch"

test -f "$1" || fail "missing file as argument. example use: ./buid.sh ../golem-unlimited/gu-hub-api.yaml"

openapi-generator generate -g python -DpackageName=gu_rest_api -DprojectName=gu-python-client -Dlibrary=asyncio -o $PWD -i "$1" --git-user-id prekucki --git-repo-id gu-python-client -DenablePostProcessFile=true --skip-validate-spec

patch -p1 < generator-fix.patch

