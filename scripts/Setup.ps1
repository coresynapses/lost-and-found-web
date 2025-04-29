if ($args.Count -eq 0) {
	Write-Host "Initialize";
	python manage.py makemigrations lostfound
	python manage.py migrate
	python manage.py database --mode 0
} else {
    switch ($arg[0]) {
	"init" {
	    Write-Host "Initialize";
	    python manage.py makemigrations lostfound
	    python manage.py migrate
	    python manage.py database --mode 0
	}
	"clear" {
	    Write-Host "Clearing database";
	    python manage.py database --mode 3
	}
	"show" {
	    Write-Host "Displaying database";
	    python manage.py database --mode 2
	}
    }
}
