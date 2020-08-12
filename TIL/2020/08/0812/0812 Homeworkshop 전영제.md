# 0812 Homeworkshop 전영제

## Homework

### prob 1

#### 1)

```
Buttons
```

#### 2)

```html
<button type="button" class="btn btn-success">Sign in</button>
```



### prob 2

#### 1)

```
Navbar
```

#### 2)

```html
    <nav class="navbar navbar-dark bg-dark justify-content-start">
        <img src="ssafy.png" alt="오류다!">
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              프로젝트
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </div>
          <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              그룹들
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </div>
          <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              더보기
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </div>
    </nav>
```



### prob 3

#### 1)

```
Pagination
```

#### 2)

``` html
	  <nav aria-label="Page navigation example text">
        <ul class="pagination text">
          <li class="page-item"><a class="page-link text" href="#">Previous</a></li>
          <li class="page-item"><a class="page-link text" href="#">1</a></li>
          <li class="page-item"><a class="page-link text" href="#">2</a></li>
          <li class="page-item"><a class="page-link text" href="#">3</a></li>
          <li class="page-item"><a class="page-link text" href="#">Next</a></li>
          <li class="page-item"><a class="page-link text" href="#">Last>></a></li>
        </ul>
      </nav>
```



### prob 4

#### 1)

``` html
Form
```

#### 2)

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <title>Document</title>
    <style>
        .end {
            display: flex;
            justify-content: flex-end;
        }

        .btn-success2 {
            color: #fff;
            background-color: #28a745;
            border-color: #28a745;
            display: flex;
            justify-content: flex-end;
        }

        .flex {
            display: flex;
        }
        .header{
            background-color:crimson;
            height: 40px;
        }
        .header-text {
            justify-content: center;
            align-items: center;
        }
        .hr {
            color: purple;
        }
        .bt-opt{
            justify-content: stretch;
        }
    </style>
</head>
<body class="container">
    <header class="header flex">
        <div class="pl-4 text-white header-text">
            <p class="">안녕</p>
        </div>
    </header>
    <h2 class="">
        SSAFY 전용 GitLab 시스템
    </h2>
    <div>
        <hr>
    </div>
    <form class="container  border">
        <div class="text-center">
            Sign in
        </div>
        <hr class="hr">
        <div class="form-group">
          <label for="exampleInputEmail1">Username or email</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Remember me</label>
          <label for="forgot" class="end">
              <a href="#">forgot your password?</a>
          </label>
        </div>
        <div class="flex bt-opt">
            <button type="submit" class="btn btn-success2 btn bt-opt">Sign In</button>
        </div>
    </form>
    
    
      



    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>


```





## Workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body class="body">
    <div>
        <nav class="navbar_y navbar-dark bg-dark nav">
            <img src="images\logo.png" alt="Error">
            <div>
                <ul class="nav">
                    <li class="nav-item">
                      <a class="nav-link_y active nav_white" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link_y nav_white" href="#">Community</a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link_y nav_white" href="#">Login</a>
                    </li>
                  </ul>
            </div>
            
        </nav>
    </div>
    <Header class="header flex header_y">
            <div class="text-center text-white ">
                <h4 class="display-2">Cinema</h4>
                <h4 class="display-2">Community</h4>
                <button type="button" class="btn btn-primary">Let's go</button>
            </div>
    </Header>
    <section class="flex justify-content-around">
        <div>
            <img src="images/web.png" alt="">
            <p class="text-center">Web</p>
        </div>
        <div>
            <img src="images/html5.png" alt="">
            <p class="text-center">HTML5</p>
        </div>
        <div>
            <img src="images/css3.png" alt="">
            <p class="text-center">CSS3</p>
        </div>
    </section>
    <footer class="f-bg flex header_y">
        <p class="text-center text-white">HTML & CSS project. Created by 전영제.2020</p>
    </footer>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>
```

