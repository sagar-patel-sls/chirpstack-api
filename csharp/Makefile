.PHONY: requirements 

all: requirements install clean-after

requirements: clean-after
	rm -rf chirpstack
	dotnet clean

install:
	dotnet build -c Release -o /app/build

clean-after:
	rm -rf obj
	rm -rf bin