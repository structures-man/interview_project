import axios from "axios";
// axios 全局配置实例
const client = axios.create({
  baseURL: "/api",
  timeout: 10000,
});
// api 接口方法
export function uploadFile(file: File) {
    // 表单提交 body 请求体
  const form = new FormData();
  form.append("file", file);
//   泛型 泛指promise resolve 值的类型
//   T 类型作为参数
  return client.post<{
    // 0 没有错误 1 错误
    code: number;
    // 错误信息
    message: string;
    // 上传成功后的数据
    data: {
      original_name: string; // 原始文件名
      saved_name: string; // 文件名要唯一
      size: number; // 文件大小
    };
  }>("/upload", form, {
    headers: {
        // 附件、 文件上传需要设置 Content-Type 为 multipart/form-data
      "Content-Type": "multipart/form-data",
    },
  });
}