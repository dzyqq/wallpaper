// 登录表单提交事件处理
document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // 阻止表单的默认提交行为

    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    // 简单验证
    if (!username || !password) {
        alert('请填写用户名和密码');
        return;
    }

    try {
        // 发送登录请求
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);  // 登录成功的反馈
            location.href = "../shipin/index.html";

        } else {
            alert(data.message);  // 错误的用户名或密码
        }
    } catch (error) {
        console.error('登录请求失败', error);
        alert('请求失败，请稍后再试');
    }
});

// 注册表单提交事件处理
document.getElementById('registerForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // 阻止表单的默认提交行为

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // 简单验证
    if (!username || !password) {
        alert('请填写用户名和密码');
        return;
    }

    try {
        // 发送注册请求
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);  // 注册成功的反馈
        } else {
            alert(data.message);  // 用户已存在或其他错误
        }
    } catch (error) {
        console.error('注册请求失败', error);
        alert('请求失败，请稍后再试');
    }
});
